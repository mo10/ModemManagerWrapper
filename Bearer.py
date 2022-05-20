from typing import Dict, Tuple

from ModemManagerWrapper.MMInterface import MMInterface
from ModemManagerWrapper.ModemManager import ModemManager


class Barer(MMInterface):
    """
    This interface provides access to specific actions that may be performed on available bearers.
    """

    def __init__(self, manager: ModemManager, instance):
        super().__init__(manager)
        self._instance = instance

    """
    Properties
    """

    @property
    def Interface(self) -> str:
        """
        The operating system name for the network data interface that provides packet data using this bearer.
        Connection managers must configure this interface depending on the IP "method" given by the "Ip4Config" or "Ip6Config" properties set by bearer activation.
        If MM_BEARER_IP_METHOD_STATIC or MM_BEARER_IP_METHOD_DHCP methods are given, the interface will be an ethernet-style interface suitable for DHCP or setting static IP configuration on, while if the MM_BEARER_IP_METHOD_PPP method is given, the interface will be a serial TTY which must then have PPP run over it.
        Since: 1.0
        """
        return self._instance.Interface

    @property
    def Connected(self) -> bool:
        """
        Indicates whether or not the bearer is connected and thus whether packet data communication using this bearer is possible.
        Since: 1.0
        """
        return self._instance.Connected

    @property
    def ConnectionError(self) -> Tuple[str, str]:
        """
        Provides additional information specifying the reason why the modem is not connected (either due to a failed connection attempt, or due to a a network initiated disconnection).
        The value is composed of two strings: the registered DBus error name, and an optional error message.
        Since: 1.18
        """
        return self._instance.ConnectionError

    @property
    def Suspended(self) -> bool:
        """
        In some devices, packet data service will be suspended while the device is handling other communication, like a voice call. If packet data service is suspended (but not deactivated) this property will be TRUE.
        Since: 1.0
        """
        return self._instance.Suspended

    @property
    def Multiplexed(self) -> bool:
        """
        This property will be TRUE if the bearer is connected through a multiplexed network link.
        Since: 1.18
        """
        return self._instance.Multiplexed

    @property
    def Ip4Config(self) -> Dict[str, object]:
        """
        If the bearer was configured for IPv4 addressing, upon activation this property contains the addressing details for assignment to the data interface.
        Mandatory items include:
            "method" A MMBearerIpMethod, given as an unsigned integer value (signature "u").

        If the bearer specifies configuration via PPP or DHCP, only the "method" item is guaranteed to be present.
        Additional items which are only applicable when using the MM_BEARER_IP_METHOD_STATIC method are:
            "address" IP address, given as a string value (signature "s").
            "prefix" Numeric CIDR network prefix (ie, 24, 32, etc), given as an unsigned integer value (signature "u").
            "dns1" IP address of the first DNS server, given as a string value (signature "s").
            "dns2" IP address of the second DNS server, given as a string value (signature "s").
            "dns3" IP address of the third DNS server, given as a string value (signature "s").
            "gateway" IP address of the default gateway, given as a string value (signature "s").

        This property may also include the following items when such information is available:
            "mtu" Maximum transmission unit (MTU), given as an unsigned integer value (signature "u").

        Since: 1.0
        """
        return dict(self._instance.Ip4Config)

    @property
    def Ip6Config(self) -> Dict[str, object]:
        """
        If the bearer was configured for IPv6 addressing, upon activation this property contains the addressing details for assignment to the data interface.
        Mandatory items include:
            "method" A MMBearerIpMethod, given as an unsigned integer value (signature "u").

        If the bearer specifies configuration via PPP or DHCP, often only the "method" item will be present. IPv6 SLAAC should be used to retrieve correct addressing and DNS information via Router Advertisements and DHCPv6. In some cases an IPv6 Link-Local "address" item will be present, which should be assigned to the data port before performing SLAAC, as the mobile network may expect SLAAC setup to use this address.
        Additional items which are usually only applicable when using the MM_BEARER_IP_METHOD_STATIC method are:
            "address" IP address, given as a string value (signature "s").
            "prefix" Numeric CIDR network prefix (ie, 24, 32, etc), given as an unsigned integer value (signature "u").
            "dns1" IP address of the first DNS server, given as a string value (signature "s").
            "dns2" IP address of the second DNS server, given as a string value (signature "s").
            "dns3" IP address of the third DNS server, given as a string value (signature "s").
            "gateway" IP address of the default gateway, given as a string value (signature "s").

        This property may also include the following items when such information is available:
            "mtu" Maximum transmission unit (MTU), given as an unsigned integer value (signature "u"). Since 1.4.

        Since: 1.0
        """
        return dict(self._instance.Ip6Config)

    @property
    def Stats(self) -> Dict[str, object]:
        """
        If the modem supports it, this property will show statistics associated to the bearer.
        There are two main different statistic types reported: either applicable to the ongoing connection, or otherwise compiled for all connections that have been done on this bearer object.
        When the connection is disconnected automatically or explicitly by the user, the values applicable to the ongoing connection will show the last values cached.
        The following items may appear in the list of statistics:
            "rx-bytes" Number of bytes received without error in the ongoing connection, given as an unsigned 64-bit integer value (signature "t").
            "tx-bytes" Number of bytes transmitted without error in the ongoing connection, given as an unsigned 64-bit integer value (signature "t").
            "duration" Duration of the ongoing connection, in seconds, given as an unsigned integer value (signature "u").
            "attempts" Total number of connection attempts done with this bearer, given as an unsigned integer value (signature "u"). Since 1.14.
            "failed-attempts" Number of failed connection attempts done with this bearer, given as an unsigned integer value (signature "u"). Since 1.14.
            "total-rx-bytes" Total number of bytes received without error in all the successful connection establishments, given as an unsigned 64-bit integer value (signature "t"). Since 1.14.
            "total-tx-bytes" Total number of bytes transmitted without error in all the successful connection establishments, given as an unsigned 64-bit integer value (signature "t"). Since 1.14.
            "total-duration" Total duration of all the successful connection establishments, in seconds, given as an unsigned integer value (signature "u"). Since 1.14.

        Since: 1.6
        """
        return dict(self._instance.Stats)

    @property
    def IpTimeout(self) -> int:
        """
        Maximum time to wait for a successful IP establishment, when PPP is used.
        Since: 1.0
        """
        return self._instance.IpTimeout

    @property
    def BearerType(self) -> int:
        """
        A MMBearerType
        Since: 1.10
        """
        return self._instance.BearerType

    @property
    def ProfileId(self) -> int:
        """
        The profile ID this bearer object is associated with, only applicable if the modem supports profile management operations, and if the bearer is connected.
        If the bearer is disconnected, or if profile management operations are not supported, -1 will be reported.
        Since: 1.18
        """
        return self._instance.ProfileId

    @property
    def Properties(self) -> Dict[str, object]:
        """
        List of settings used to create the bearer.
        Bearers may be implicitly created (e.g. the default initial EPS bearer created during the network registration process in 4G and 5G networks) or explicitly created by the user (e.g. via the CreateBearer() or Connect() calls).
        The following settings apply to 3GPP (GSM/UMTS/LTE/5GNR) devices:
            "apn" The Access Point Name to use in the connection, given as a string value (signature "s").
            "ip-type" The IP addressing type to use, given as a MMBearerIpFamily value (signature "u").
            "apn-type" The purposes of the specified APN, given as a MMBearerApnType value (signature "u").
            "allowed-auth" The authentication method to use, given as a MMBearerAllowedAuth value (signature "u").
            "user" The user name (if any) required by the network, given as a string value (signature "s").
            "password" The password (if any) required by the network, given as a string value (signature "s").
            "profile-id" The ID of the 3GPP profile to connect to (signature "i"), as given in the profile list. In this case, if additional profile settings are given in the properties and they already exist in the profile (e.g. "apn"), the new settings will be explicitly ignored; the settings stored in the profile itself always take preference. The value -1 is used to indicate an invalid or uninitialized profile id. Since 1.18.

        The following settings apply to 3GPP2 (CDMA/EVDO) devices:
            "rm-protocol" The protocol of the Rm interface, given as a MMModemCdmaRmProtocol value (signature "u").

        The following settings apply to all devices types:
            "allow-roaming" Specifies whether the connections are allowed even when the device is registered in a roaming network, given as a boolean value (signature "b").
            "multiplex" The multiplex support requested by the user, given as a MMBearerMultiplexSupport value (signature "u"). Since 1.18.

        The following settings are no longer supported, but they are kept on the interface for compatibility purposes:
            "number" Number to dial for the data connection, given as a string value (signature "s"). Deprecated since version 1.10.0.

        Since: 1.0
        """
        return dict(self._instance.Properties)
