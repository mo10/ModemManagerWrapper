from typing import List, Tuple

from MMInterface import MMInterface
from ModemManager import ModemManager


class SIM(MMInterface):
    """
    The SIM interface handles communication with SIM, USIM, and RUIM (CDMA SIM) cards.
    """

    def __init__(self, manager: ModemManager, instance):
        super().__init__(manager)
        self._instance = instance

    def SendPin(self, pin: str):
        """
        Send the PIN to unlock the SIM card.

        Since: 1.0
        :param pin: A string containing the PIN code.
        """
        self._instance.SendPin(pin)

    def SendPuk(self, puk: str, pin: str):
        """
        Send the PUK and a new PIN to unlock the SIM card.

        Since: 1.0
        :param puk: A string containing the PUK code.
        :param pin: A string containing the PIN code.
        """
        self._instance.SendPuk(puk, pin)

    def EnablePin(self, pin: str, enable: bool):
        """
        Enable or disable the PIN checking.

        Since: 1.0
        :param pin: A string containing the PIN code.
        :param enable: True to enable PIN checking, False otherwise.
        """
        self._instance.EnablePin(pin, enable)

    def ChangePin(self, old_pin: str, new_pin: str):
        """
        Change the PIN code.

        Since: 1.0
        :param old_pin: A string containing the current PIN code.
        :param new_pin: A string containing the new PIN code.
        """
        self._instance.ChangePin(old_pin, new_pin)

    def SetPreferredNetworks(self, preferred_networks: List[Tuple[str, int]]):
        """
        Stores the provided preferred network list to the SIM card.
        Each entry contains an operator id string ("MCCMNC") consisting of 5 or 6 digits,
        and an MMModemAccessTechnology mask to store to SIM card if supported.

        This method removes any pre-existing entries of the preferred network list.
        Note that even if this operation fails, the preferred network list on the SIM card may have changed.
        Read the PreferredNetworks property to get the up-to-date list.

        Since: 1.18
        :param preferred_networks:
        """
        self._instance.SetPreferredNetworks(preferred_networks)

    @property
    def Active(self) -> bool:
        """
        Boolean indicating whether the SIM is currently active.

        On systems that support Multi SIM Single Standby, only one SIM may be active at any given time,
        which will be the one considered primary.

        On systems that support Multi SIM Multi Standby, more than one SIM may be active at any given time,
        but only one of them is considered primary.

        Since: 1.16
        :return: bool
        """
        return self._instance.Active

    @property
    def SimIdentifier(self) -> str:
        """
        The ICCID of the SIM card.

        This may be available before the PIN has been entered depending on the device itself.

        Since: 1.0
        :return: string
        """
        return self._instance.SimIdentifier

    @property
    def Imsi(self) -> str:
        """
        The IMSI of the SIM card, if any.

        Since: 1.0
        :return: string
        """
        return self._instance.Imsi

    @property
    def Eid(self) -> str:
        """
        The EID of the SIM card, if any.

        Since: 1.16
        :return: string
        """
        return self._instance.Eid

    @property
    def OperatorIdentifier(self) -> str:
        return self._instance.OperatorIdentifier

    @property
    def OperatorName(self) -> str:
        """
        The name of the network operator, as given by the SIM card, if known.

        Since: 1.0
        :return: string
        """
        return self._instance.OperatorName

    @property
    def EmergencyNumbers(self) -> List[str]:
        """
        List of emergency numbers programmed in the SIM card.

        These numbers should be treated as numbers for emergency calls in addition to 112 and 911.

        Since: 1.12
        :return: List[str]
        """
        return self._instance.EmergencyNumbers

    @property
    def PreferredNetworks(self) -> List[Tuple[str, int]]:
        """
        List of preferred networks with access technologies configured in the SIM card.

        Each entry contains an operator id string ("MCCMNC") consisting of 5 or 6 digits, and an MMModemAccessTechnology mask. If the SIM card does not support access technology storage, the mask will be set to MM_MODEM_ACCESS_TECHNOLOGY_UNKNOWN.

        Since: 1.18
        :return:
        """
        return self._instance.PreferredNetworks
