from typing import Dict, Tuple, List

from ModemManagerWrapper.MMInterface import MMInterface
from ModemManagerWrapper.ModemManager import ModemManager
from ModemManagerWrapper.MMEnum import MMModemPowerState, MMModemCapability, MMModemBand, MMModemPortType, MMModemLock, \
    MMModemState, MMModemStateFailedReason, MMModemAccessTechnology, MMModemMode, MMBearerIpFamily


class Modem(MMInterface):
    """
    The Modem interface controls the status and actions in a given modem object.
    This interface will always be available as long a the modem is considered valid.
    """

    def __init__(self, manager: ModemManager, instance):
        super().__init__(manager)
        self._instance = instance

    """
    Methods
    """

    def Enable(self, enable: bool):
        """
        Enable or disable the modem.
        When enabled, the modem's radio is powered on and data sessions, voice calls, location services, and Short Message Service may be available.
        When disabled, the modem enters low-power state and no network-related operations are available.
        Since: 1.0
        :param enable: True to enable the modem and False to disable it.
        """
        self._instance.Enable(enable)

    def ListBearers(self):
        """
        List configured packet data bearers (EPS Bearers, PDP Contexts, or CDMA2000 Packet Data Sessions).
        Since: 1.0
        Deprecated: 1.10.0. Use "Bearers" property instead.
        :return: The list of bearer object paths.
        """
        return self._instance.ListBearers()

    def CreateBearer(self, properties: Dict[str, object]) -> str:
        """
        Create a new packet data bearer using the given characteristics.
        This request may fail if the modem does not support additional bearers, if too many bearers are already defined, or if properties are invalid.
        The properties allowed are any of the ones defined in the bearer properties.
        Since: 1.0
        :param properties: Dictionary of properties needed to get the bearer connected.
        :return: On success, the object path of the newly created bearer.
        """
        return self._instance.CreateBearer(properties)

    def DeleteBearer(self, bearer: str):
        """
        Delete an existing packet data bearer.
        If the bearer is currently active and providing packet data server, it will be disconnected and that packet data service will terminate.
        Since: 1.0
        :param bearer: Object path of the bearer to delete.
        """
        self._instance.DeleteBearer(bearer)

    def Reset(self):
        """
        Clear non-persistent configuration and state, and return the device to a newly-powered-on state.
        This command may power-cycle the device.
        Since: 1.0
        """
        self._instance.Reset()

    def FactoryReset(self, code: str):
        """
        Clear the modem's configuration (including persistent configuration and state), and return the device to a factory-default state.
        If not required by the modem, code may be ignored.
        This command may or may not power-cycle the device.
        Since: 1.0
        :param code: Carrier-supplied code required to reset the modem.
        """
        self._instance.FactoryReset(code)

    def SetPowerState(self, state: MMModemPowerState):
        """
        Set the power state of the modem. This action can only be run when the modem is in MM_MODEM_STATE_DISABLED state.
        Since: 1.0
        :param state: A MMModemPowerState value, to specify the desired power state.
        """
        self._instance.SetPowerState(state.value)

    def SetCurrentCapabilities(self, capabilities: MMModemCapability):
        """
        Set the capabilities of the device.
        The given bitmask should be supported by the modem, as specified in the "SupportedCapabilities" property.
        This command may power-cycle the device.
        Since: 1.0
        :param capabilities: Bitmask of MMModemCapability values, to specify the capabilities to use.
        """
        self._instance.SetCurrentCapabilities(capabilities.value)

    def SetCurrentModes(self, modes: Tuple[int, int]):
        """
        Set the access technologies (e.g. 2G/3G/4G preference) the device is currently allowed to use when connecting to a network.
        The given combination should be supported by the modem, as specified in the "SupportedModes" property.
        Since: 1.0
        :param modes: A pair of MMModemMode values, where the first one is a bitmask of allowed modes, and the second one the preferred mode, if any.
        """
        self._instance.SetCurrentModes(modes)

    def SetCurrentBands(self, bands: List[MMModemBand]):
        """
        Set the radio frequency and technology bands the device is currently allowed to use when connecting to a network.
        Since: 1.0
        :param bands: List of MMModemBand values, to specify the bands to be used.
        """
        self._instance.SetCurrentBands([v.value for v in bands])

    def SetPrimarySimSlot(self, sim_slot: int):
        """
        Selects which SIM slot to be considered as primary, on devices that expose multiple slots in the "SimSlots" property.
        When the switch happens the modem may require a full device reprobe, so the modem object in DBus will get removed, and recreated once the selected SIM slot is in use.
        There is no limitation on which SIM slot to select, so the user may also set as primary a slot that doesn't currently have any valid SIM card inserted.
        Since: 1.16
        :param sim_slot: SIM slot number to set as primary.
        """
        self._instance.SetPrimarySimSlot(sim_slot)

    def Command(self, cmd: str, timeout: int) -> str:
        """
        Send an arbitrary AT command to a modem and get the response.
        Note that using this interface call is only allowed when running ModemManager in debug mode or if the project was built using the with-at-command-via-dbus configure option.
        Since: 1.0
        :param cmd: The command string, e.g. "AT+GCAP" or "+GCAP" (leading AT is inserted if necessary).
        :param timeout: The number of seconds to wait for a response.
        :return: The modem's response.
        """
        return self._instance.Command(cmd, timeout)

    """
    Properties
    """

    @property
    def Sim(self) -> str:
        """
        The path of the primary active SIM object available in this device, if any.
        This SIM object is the one used for network registration and data connection setup.
        If multiple org.freedesktop.ModemManager1.Modem.SimSlots are supported, the org.freedesktop.ModemManager1.Modem.PrimarySimSlot index value specifies which is the slot number where this SIM card is available.
        Since: 1.0
        """
        return self._instance.Sim

    @property
    def SimSlots(self) -> List[str]:
        """
        The list of SIM slots available in the system, including the SIM object paths if the cards are present. If a given SIM slot at a given index doesn't have a SIM card available, an empty object path will be given.
        The length of this array of objects will be equal to the amount of available SIM slots in the system, and the index in the array is the slot index.
        This list includes the SIM object considered as primary active SIM slot (org.freedesktop.ModemManager1.Modem.Sim) at index org.freedesktop.ModemManager1.Modem.ActiveSimSlot.
        Since: 1.16
        """
        return self._instance.SimSlots

    @property
    def PrimarySimSlot(self) -> int:
        """
        The index of the primary active SIM slot in the org.freedesktop.ModemManager1.Modem.SimSlots array, given in the [1,N] range.
        If multiple SIM slots aren't supported, this property will report value 0.
        In a Multi SIM Single Standby setup, this index identifies the only SIM that is currently active. All the remaining slots will be inactive.
        In a Multi SIM Multi Standby setup, this index identifies the active SIM that is considered primary, i.e. the one that will be used when a data connection is setup.
        Since: 1.16
        """
        return self._instance.PrimarySimSlot

    @property
    def Bearers(self) -> List[str]:
        """
        The list of bearer object paths (EPS Bearers, PDP Contexts, or CDMA2000 Packet Data Sessions) as requested by the user.
        This list does not include the initial EPS bearer details (see "InitialEpsBearer").
        Since: 1.2
        """
        return self._instance.Bearers

    @property
    def SupportedCapabilities(self) -> List[MMModemCapability]:
        """
        List of MMModemCapability bitmasks, specifying the combinations of generic family of access technologies the modem supports.
        If the modem doesn't allow changing the current capabilities, the list will report one single entry with the same bitmask as in "CurrentCapabilities".
        Only multimode devices implementing both 3GPP (GSM/UMTS/LTE/5GNR) and 3GPP2 (CDMA/EVDO) specs will report more than one combination of capabilities.
        Since: 1.0
        """
        return self._instance.SupportedCapabilities

    @property
    def CurrentCapabilities(self) -> MMModemCapability:
        """
        Bitmask of MMModemCapability values, specifying the currently used generic family of access technologies.
        This bitmask will be one of the ones listed in "SupportedCapabilities".
        Since: 1.0
        """
        return self._instance.CurrentCapabilities

    @property
    def MaxBearers(self) -> int:
        """
        The maximum number of defined packet data bearers the modem supports.
        This is not the number of active/connected bearers the modem supports, but simply the number of bearers that may be defined at any given time. For example, POTS and CDMA2000-only devices support only one bearer, while GSM/UMTS devices typically support three or more, and any LTE-capable device (whether LTE-only, GSM/UMTS-capable, and/or CDMA2000-capable) also typically support three or more.
        Deprecated: 1.18.0. There is no way to query the modem how many bearers it supports, so the value exposed in this property in all the different implementations is always equal to the value in "MaxActiveBearers", so there is no point in using this property.
        Since: 1.0
        """
        return self._instance.MaxBearers

    @property
    def MaxActiveBearers(self) -> int:
        """
        The maximum number of active MM_BEARER_TYPE_DEFAULT bearers that may be explicitly enabled by the user without multiplexing support.
        POTS and CDMA2000-only devices support one active bearer, while GSM/UMTS and LTE/5GNR capable devices (including 3GPP+3GPP3 multimode devices) may support one or more active bearers, depending on the amount of physical ports exposed by the device.
        Since: 1.0
        """
        return self._instance.MaxActiveBearers

    @property
    def MaxActiveMultiplexedBearers(self) -> int:
        """
        The maximum number of active MM_BEARER_TYPE_DEFAULT bearers that may be explicitly enabled by the user with multiplexing support on one single network interface.
        If the modem doesn't support multiplexing of data sessiones, a value of 0 will be reported.
        Since: 1.18
        """
        return self._instance.MaxActiveMultiplexedBearers

    @property
    def Manufacturer(self) -> str:
        """
        The equipment manufacturer, as reported by the modem.
        Since: 1.0
        """
        return self._instance.Manufacturer

    @property
    def Model(self) -> str:
        """
        The equipment model, as reported by the modem.
        Since: 1.0
        """
        return self._instance.Model

    @property
    def Revision(self) -> str:
        """
        The revision identification of the software, as reported by the modem.
        Since: 1.0
        """
        return self._instance.Revision

    @property
    def CarrierConfiguration(self) -> str:
        """
        The description of the carrier-specific configuration (MCFG) in use by the modem.
        Since: 1.12
        """
        return self._instance.CarrierConfiguration

    @property
    def CarrierConfigurationRevision(self) -> str:
        """
        The revision identification of the carrier-specific configuration (MCFG) in use by the modem.
        Since: 1.12
        """
        return self._instance.CarrierConfigurationRevision

    @property
    def HardwareRevision(self) -> str:
        """
        The revision identification of the hardware, as reported by the modem.
        Since: 1.8
        """
        return self._instance.HardwareRevision

    @property
    def DeviceIdentifier(self) -> str:
        """
        A best-effort device identifier based on various device information like model name, firmware revision, USB/PCI/PCMCIA IDs, and other properties.
        This ID is not guaranteed to be unique and may be shared between identical devices with the same firmware, but is intended to be "unique enough" for use as a casual device identifier for various user experience operations.
        This is not the device's IMEI or ESN since those may not be available before unlocking the device via a PIN.
        Since: 1.0
        """
        return self._instance.DeviceIdentifier

    @property
    def Device(self) -> str:
        """
        The physical modem device reference (ie, USB, PCI, PCMCIA device), which may be dependent upon the operating system.
        In Linux for example, this points to a sysfs path of the usb_device object.
        This value may also be set by the user using the MM_ID_PHYSDEV_UID udev tag (e.g. binding the tag to a specific sysfs path).
        Since: 1.0
        """
        return self._instance.Device

    @property
    def Drivers(self) -> List[str]:
        """
        The Operating System device drivers handling communication with the modem hardware.
        Since: 1.0
        """
        return self._instance.Drivers

    @property
    def Plugin(self) -> str:
        """
        The name of the plugin handling this modem.
        Since: 1.0
        """
        return self._instance.Plugin

    @property
    def PrimaryPort(self) -> str:
        """
        The name of the primary port using to control the modem.
        Since: 1.0
        """
        return self._instance.PrimaryPort

    @property
    def Ports(self) -> List[Tuple[str, MMModemPortType]]:
        """
        The list of ports in the modem, given as an array of string and unsigned integer pairs. The string is the port name or path, and the integer is the port type given as a MMModemPortType value.
        Since: 1.0
        """
        return self._instance.Ports

    @property
    def EquipmentIdentifier(self) -> str:
        """
        The identity of the device.
        This will be the IMEI number for GSM devices and the hex-format ESN/MEID for CDMA devices.
        Since: 1.0
        """
        return self._instance.EquipmentIdentifier

    @property
    def UnlockRequired(self) -> MMModemLock:
        """
        Current lock state of the device, given as a MMModemLock value.
        Since: 1.0
        """
        return self._instance.UnlockRequired

    @property
    def UnlockRetries(self) -> Dict[MMModemLock, int]:
        """
        A dictionary in which the keys are MMModemLock flags, and the values are integers giving the number of PIN tries remaining before the code becomes blocked (requiring a PUK) or permanently blocked. Dictionary entries exist only for the codes for which the modem is able to report retry counts.
        Since: 1.0
        """
        return self._instance.UnlockRetries

    @property
    def State(self) -> MMModemState:
        """
        Overall state of the modem, given as a MMModemState value.
        If the device's state cannot be determined, MM_MODEM_STATE_UNKNOWN will be reported.
        Since: 1.0
        """
        return self._instance.State

    @property
    def StateFailedReason(self) -> MMModemStateFailedReason:
        """
        Error specifying why the modem is in MM_MODEM_STATE_FAILED state, given as a MMModemStateFailedReason value.
        Since: 1.0
        """
        return self._instance.StateFailedReason

    @property
    def AccessTechnologies(self) -> MMModemAccessTechnology:
        """
        Bitmask of MMModemAccessTechnology values, specifying the current network access technologies used by the device to communicate with the network.
        If the device's access technology cannot be determined, MM_MODEM_ACCESS_TECHNOLOGY_UNKNOWN will be reported.
        Since: 1.0

        """
        return self._instance.AccessTechnologies

    @property
    def SignalQuality(self) -> Tuple[int, bool]:
        """
        Signal quality in percent (0 - 100) of the dominant access technology the device is using to communicate with the network. Always 0 for POTS devices.
        The additional boolean value indicates if the quality value given was recently taken.
        Since: 1.0
        """
        return self._instance.SignalQuality

    @property
    def OwnNumbers(self) -> List[str]:
        """
        List of numbers (e.g. MSISDN in 3GPP) being currently handled by this modem.
        Since: 1.0
        """
        return self._instance.OwnNumbers

    @property
    def PowerState(self) -> MMModemPowerState:
        """
        A MMModemPowerState value specifying the current power state of the modem.
        Since: 1.0
        """
        return self._instance.PowerState

    @property
    def SupportedModes(self) -> List[Tuple[MMModemMode, MMModemMode]]:
        """
        This property exposes the supported mode combinations, given as an array of unsigned integer pairs, where:

            The first integer is a bitmask of MMModemMode values, specifying the allowed modes.
            The second integer is a single MMModemMode, which specifies the preferred access technology, among the ones defined in the allowed modes.

        Since: 1.0
        """
        return self._instance.SupportedModes

    @property
    def CurrentModes(self) -> Tuple:
        """
        A pair of MMModemMode values, where the first one is a bitmask specifying the access technologies (eg 2G/3G/4G) the device is currently allowed to use when connecting to a network, and the second one is the preferred mode of those specified as allowed.
        The pair must be one of those specified in "SupportedModes".
        Since: 1.0
        """
        return self._instance.CurrentModes

    @property
    def SupportedBands(self) -> List[MMModemBand]:
        """
        List of MMModemBand values, specifying the radio frequency and technology bands supported by the device.
        For POTS devices, only the MM_MODEM_BAND_ANY mode will be returned.
        Since: 1.0
        """
        return self._instance.SupportedBands

    @property
    def CurrentBands(self) -> List[MMModemBand]:
        """
        List of MMModemBand values, specifying the radio frequency and technology bands the device is currently using when connecting to a network.
        It must be a subset of "SupportedBands".
        Since: 1.0
        """
        return self._instance.CurrentBands

    @property
    def SupportedIpFamilies(self) -> MMBearerIpFamily:
        """
        Bitmask of MMBearerIpFamily values, specifying the IP families supported by the device.
        Since: 1.0
        """
        return self._instance.SupportedIpFamilies
