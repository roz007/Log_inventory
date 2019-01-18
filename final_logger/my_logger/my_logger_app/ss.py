@api_view(["POST"])
def user_event_register(request):
    """
    Register a user to new event after checking various constraints
    :param request:
    :return:
    
    """
    try:
        selected_event = Event.objects.get(id=request.data['event_id'])
    except Event.DoesNotExist:
        return Response({'error': 'Event Doesnt Exist'})

    is_already_registered_for_same_event = EventRegistration.objects.filter(
        user=request.user, event=selected_event).count() != 0
    current_time = timezone.now()

    if is_already_registered_for_same_event:
        return Response({'error': 'User Already Registered for same event'})

    elif selected_event.start_time < current_time:
        return Response({'error': 'Event has already started'})

    elif selected_event.total_people > selected_event.max_people:
        return Response({'error': 'Event is full'})

    elif check_overlaping_event(selected_event, request.user):
        return Response({'error': 'User has another event in the same time'})

    else:
        EventRegistration.objects.create(
            event=selected_event, user=request.user)
        current_user_count = selected_event.total_people
        Event.objects.filter(
            id=request.data['event_id']).update(
                total_people=current_user_count + 1)
        return Response(
            {
                'message':
                    f'User {request.user.username} has successfully registered fot Event : {selected_event.Event_name}'
            })