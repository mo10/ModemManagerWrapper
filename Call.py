from typing import Dict

from MMInterface import MMInterface
from ModemManager import ModemManager
from MMEnums import MMCallState, MMCallStateReason, MMCallDirection


class Call(MMInterface):
    """
    The Call interface Defines operations and properties of a single Call.
    """

    def __init__(self, manager: ModemManager, instance):
        super().__init__(manager)
        self._instance = instance

    def Start(self):
        """
        If the outgoing call has not yet been started, start it.

        Applicable only if state is MM_CALL_STATE_UNKNOWN and direction is MM_CALL_DIRECTION_OUTGOING.

        Since: 1.6
        """
        self._instance.Start()

    def Accept(self):
        """
        Accept incoming call (answer).

        Applicable only if state is MM_CALL_STATE_RINGING_IN and direction is MM_CALL_DIRECTION_INCOMING.

        Since: 1.6
        """
        self._instance.Accept()

    def Deflect(self, number: str):
        """
        Deflect an incoming or waiting call to a new number. This call will be considered terminated once the deflection is performed.

        Applicable only if state is MM_CALL_STATE_RINGING_IN or MM_CALL_STATE_WAITING and direction is MM_CALL_DIRECTION_INCOMING.

        Since: 1.12
        :param number: new number where the call will be deflected.
        """
        self._instance.Deflect(number)

    def JoinMultiparty(self):
        """
        Join the currently held call into a single multiparty call with another already active call.

        The calls will be flagged with the 'Multiparty' property while they are part of the multiparty call.

        Applicable only if state is MM_CALL_STATE_HELD.

        Since: 1.12
        """
        self._instance.JoinMultiparty()

    def LeaveMultiparty(self):
        """
        If this call is part of an ongoing multiparty call, detach it from the multiparty call,
        put the multiparty call on hold, and activate this one alone.
        This operation makes this call private again between both ends of the call.

        Applicable only if state is MM_CALL_STATE_ACTIVE or MM_CALL_STATE_HELD and the call is a multiparty call.

        Since: 1.12
        """
        self._instance.LeaveMultiparty()

    def Hangup(self):
        """
        Hangup the active call.

        Applicable only if state is MM_CALL_STATE_UNKNOWN.

        Since: 1.6
        """
        self._instance.Hangup()

    def SendDtmf(self, dtmf: str):
        """
        Send a DTMF tone (Dual Tone Multi-Frequency) (only on supported modem).

        Applicable only if state is MM_CALL_STATE_ACTIVE.

        Since: 1.6
        :param dtmf: DTMF tone identifier [0-9A-D*#].
        """
        self._instance.SendDtmf(dtmf)

    @property
    def State(self) -> MMCallState:
        """
        A MMCallState value, describing the state of the call.

        Since: 1.6
        :return: MMCallState
        """
        return MMCallState(self._instance.State)

    @property
    def StateReason(self) -> MMCallStateReason:
        """
        A MMCallStateReason value, describing why the state is changed.

        Since: 1.6
        :return: MMCallStateReason
        """
        return MMCallStateReason(self._instance.StateReason)

    @property
    def Direction(self) -> MMCallDirection:
        """
        A MMCallDirection value, describing the direction of the call.

        Since: 1.6
        :return: MMCallDirection
        """
        return MMCallDirection(self._instance.Direction)

    @property
    def Number(self) -> str:
        """
        The remote phone number.

        Since: 1.6
        :return: string
        """
        return self._instance.Number

    @property
    def Multiparty(self) -> bool:
        """
        Whether the call is currently part of a multiparty conference call.

        Since: 1.12
        :return: bool
        """
        return self._instance.Multiparty

    @property
    def AudioPort(self) -> str:
        """
        If call audio is routed via the host, the name of the kernel device that provides the audio. For example, with certain Huawei USB modems, this property might be "ttyUSB2" indicating audio is available via ttyUSB2 in the format described by the AudioFormat property.

        Since: 1.10
        :return: string
        """
        return self._instance.AudioPort

    @property
    def AudioFormat(self) -> Dict[str, object]:
        """
        If call audio is routed via the host, a description of the audio format supported by the audio port.

        This property may include the following items:
            "encoding"
            The audio encoding format. For example, "pcm" for PCM audio.

            "resolution"
            The sampling precision and its encoding format. For example, "s16le" for signed 16-bit little-endian samples.

            "rate"
            The sampling rate as an unsigned integer. For example, 8000 for 8000hz.
        Since: 1.10
        :return:
        """
        return dict(self._instance.AudioFormat)
