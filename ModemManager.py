from typing import List, Tuple, Dict

from gi.repository import GLib
from pydbus import SystemBus

from ModemManagerWrapper.MMInterface import MMInterface
from ModemManagerWrapper.Modem import Modem


class ModemManager(MMInterface):
    """
    The Manager interface allows controlling and querying the status of the ModemManager daemon.
    """

    def __init__(self, main_loop=None, system_bus=None):
        super().__init__(self)
        if main_loop:
            self._loop = main_loop
        else:
            self._loop = GLib.MainLoop()
        if system_bus:
            self._bus = system_bus
        else:
            self._bus = SystemBus()

        self._instance = self.get_object(None)

    @property
    def modems(self):
        modems = []
        for path in self.GetManagedObjects().keys():
            modem = self.get_object(path)
            modems.append(Modem(self, modem))

        return modems

    """
    Methods
    """

    def ScanDevices(self):
        """
        Start a new scan for connected modem devices.

        Since: 1.0
        """
        return self._instance.ScanDevices()

    def SetLogging(self, level: str):
        """
        Set logging verbosity.

        Since: 1.0
        :param level: One of "ERR", "WARN", "INFO", "DEBUG".
        """
        return self._instance.SetLogging(level)

    def ReportKernelEvent(self, properties: List[Tuple[str, object]]):
        """
        Reports a kernel event to ModemManager.

        This method is only available if udev is not being used to report kernel events.

        The properties dictionary is composed of key/value string pairs. The possible keys are:
            action
            The type of action, given as a string value (signature "s"). This parameter is MANDATORY.
                add
                A new kernel device has been added.
                remove
                An existing kernel device has been removed.

            name
            The device name, given as a string value (signature "s"). This parameter is MANDATORY.

            subsystem
            The device subsystem, given as a string value (signature "s"). This parameter is MANDATORY.

            uid
            The unique ID of the physical device, given as a string value (signature "s").
            This parameter is OPTIONAL, if not given the sysfs path of the physical device will be used.
            This parameter must be the same for all devices exposed by the same physical device.

        Since: 1.8
        :param properties:
        :return:
        """
        return self._instance.ReportKernelEvent(properties)

    def InhibitDevice(self, uid: str, inhibit: bool):
        """
        org.freedesktop.ModemManager1.Modem:Device property. inhibit: TRUE to inhibit the modem and FALSE to uninhibit it.

        Inhibit or uninhibit the device.

        When the modem is inhibited ModemManager will close all its ports and unexport it from the bus,
        so that users of the interface are no longer able to operate with it.

        This operation binds the inhibition request to the existence of the caller in the DBus bus.
        If the caller disappears from the bus, the inhibition will automatically removed.

        Since: 1.10
        :param uid: the unique ID of the physical device, given in the
        :param inhibit:
        """
        return self._instance.InhibitDevice(uid, inhibit)

    def GetManagedObjects(self) -> Dict:
        return self._instance.GetManagedObjects()

    """
    Properties
    """

    @property
    def Version(self) -> str:
        """
        The runtime version of the ModemManager daemon.

        Since: 1.10
        :return: string
        """
        return self._instance.Version
