from django.dispatch import Signal

state_audit_signal = Signal(providing_args=["user", "change"])
state_audit_signal.send(sender='ME', user='asnim', change='hi')
print("signal")