from enum import Enum


class MMBearerType(Enum):
    """
    Type of context (2G/3G) or bearer (4G).

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_BEARER_TYPE_UNKNOWN = 0
    """
    Unknown bearer.
    """
    MM_BEARER_TYPE_DEFAULT = 1
    """
    Primary context (2G/3G) or default bearer (4G), defined by the user of the API.
    """
    MM_BEARER_TYPE_DEFAULT_ATTACH = 2
    """
    The initial default bearer established during LTE attach procedure, automatically connected as long as the device is regitered in the LTE network.
    """
    MM_BEARER_TYPE_DEDICATED = 3
    """
    Secondary context (2G/3G) or dedicated bearer (4G), defined by the user of the API. These bearers use the same IP address used by a primary context or default bearer and provide a dedicated flow for specific traffic with different QoS settings.
    """


class MMBearerIpFamily(Enum):
    """
    Type of IP family to be used in a given Bearer.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_BEARER_IP_FAMILY_NONE = 0
    """
    None or unknown.
    """
    MM_BEARER_IP_FAMILY_IPV4 = 1
    """
    IPv4.
    """
    MM_BEARER_IP_FAMILY_IPV6 = 2
    """
    IPv6.
    """
    MM_BEARER_IP_FAMILY_IPV4V6 = 3
    """
    IPv4 and IPv6.
    """
    MM_BEARER_IP_FAMILY_ANY = 4
    """
    Mask specifying all IP families.
    """


class MMBearerIpMethod(Enum):
    """
    Type of IP method configuration to be used in a given Bearer.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_BEARER_IP_METHOD_UNKNOWN = 0
    """
    Unknown method.
    """
    MM_BEARER_IP_METHOD_PPP = 1
    """
    Use PPP to get IP addresses and DNS information. For IPv6, use PPP to retrieve the 64-bit Interface Identifier, use the IID to construct an IPv6 link-local address by following RFC 5072, and then run DHCP over the PPP link to retrieve DNS settings.
    """
    MM_BEARER_IP_METHOD_STATIC = 2
    """
    Use the provided static IP configuration given by the modem to configure the IP data interface. Note that DNS servers may not be provided by the network or modem firmware.
    """
    MM_BEARER_IP_METHOD_DHCP = 3
    """
    Begin DHCP or IPv6 SLAAC on the data interface to obtain any necessary IP configuration details that are not already provided by the IP configuration. For IPv4 bearers DHCP should be used. For IPv6 bearers SLAAC should be used, and the IP configuration may already contain a link-local address that should be assigned to the interface before SLAAC is started to obtain the rest of the configuration.
    """


class MMBearerAllowedAuth(Enum):
    """
    Allowed authentication methods when authenticating with the network.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_BEARER_ALLOWED_AUTH_UNKNOWN = 0
    """
    Unknown.
    """
    MM_BEARER_ALLOWED_AUTH_NONE = 1
    """
    None.
    """
    MM_BEARER_ALLOWED_AUTH_PAP = 2
    """
    PAP.
    """
    MM_BEARER_ALLOWED_AUTH_CHAP = 3
    """
    CHAP.
    """
    MM_BEARER_ALLOWED_AUTH_MSCHAP = 4
    """
    MS-CHAP.
    """
    MM_BEARER_ALLOWED_AUTH_MSCHAPV2 = 5
    """
    MS-CHAP v2.
    """
    MM_BEARER_ALLOWED_AUTH_EAP = 6
    """
    EAP.
    """


class MMBearerMultiplexSupport(Enum):
    """
    Multiplex support requested by the user.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_BEARER_MULTIPLEX_SUPPORT_UNKNOWN = 0
    """
    Unknown.
    """
    MM_BEARER_MULTIPLEX_SUPPORT_NONE = 1
    """
    No multiplex support should be used.
    """
    MM_BEARER_MULTIPLEX_SUPPORT_REQUESTED = 2
    """
    If available, multiplex support should be used.
    """
    MM_BEARER_MULTIPLEX_SUPPORT_REQUIRED = 3
    """
    Multiplex support must be used or otherwise the connection attempt will fail.
    """


class MMBearerApnType(Enum):
    """
    Purpose of the APN used in a given Bearer.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_BEARER_APN_TYPE_NONE = 0
    """
    Unknown or unsupported.
    """
    MM_BEARER_APN_TYPE_INITIAL = 1
    """
    APN used for the initial attach procedure.
    """
    MM_BEARER_APN_TYPE_DEFAULT = 2
    """
    Default connection APN providing access to the Internet.
    """
    MM_BEARER_APN_TYPE_IMS = 3
    """
    APN providing access to IMS services.
    """
    MM_BEARER_APN_TYPE_MMS = 4
    """
    APN providing access to MMS services.
    """
    MM_BEARER_APN_TYPE_MANAGEMENT = 5
    """
    APN providing access to over-the-air device management procedures.
    """
    MM_BEARER_APN_TYPE_VOICE = 6
    """
    APN providing access to voice-over-IP services.
    """
    MM_BEARER_APN_TYPE_EMERGENCY = 7
    """
    APN providing access to emergency services.
    """
    MM_BEARER_APN_TYPE_PRIVATE = 8
    """
    APN providing access to private networks.
    """


class MMCallDirection(Enum):
    """
    Direction of the call.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_CALL_DIRECTION_UNKNOWN = 0
    """
    unknown.
    """
    MM_CALL_DIRECTION_INCOMING = 1
    """
    call from network.
    """
    MM_CALL_DIRECTION_OUTGOING = 2
    """
    call to network.
    """


class MMCallState(Enum):
    """
    State of Call.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_CALL_STATE_UNKNOWN = 0
    """
    default state for a new outgoing call.
    """
    MM_CALL_STATE_DIALING = 1
    """
    outgoing call started. Wait for free channel.
    """
    MM_CALL_STATE_RINGING_OUT = 2
    """
    outgoing call attached to GSM network, waiting for an answer.
    """
    MM_CALL_STATE_RINGING_IN = 3
    """
    incoming call is waiting for an answer.
    """
    MM_CALL_STATE_ACTIVE = 4
    """
    call is active between two peers.
    """
    MM_CALL_STATE_HELD = 5
    """
    held call (by +CHLD AT command).
    """
    MM_CALL_STATE_WAITING = 6
    """
    waiting call (by +CCWA AT command).
    """
    MM_CALL_STATE_TERMINATED = 7
    """
    call is terminated.
    """


class MMCallStateReason(Enum):
    """
    Reason for the state change in the call.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_CALL_STATE_REASON_UNKNOWN = 0
    """
    Default value for a new outgoing call.
    """
    MM_CALL_STATE_REASON_OUTGOING_STARTED = 1
    """
    Outgoing call is started.
    """
    MM_CALL_STATE_REASON_INCOMING_NEW = 2
    """
    Received a new incoming call.
    """
    MM_CALL_STATE_REASON_ACCEPTED = 3
    """
    Dialing or Ringing call is accepted.
    """
    MM_CALL_STATE_REASON_TERMINATED = 4
    """
    Call is correctly terminated.
    """
    MM_CALL_STATE_REASON_REFUSED_OR_BUSY = 5
    """
    Remote peer is busy or refused call.
    """
    MM_CALL_STATE_REASON_ERROR = 6
    """
    Wrong number or generic network error.
    """
    MM_CALL_STATE_REASON_AUDIO_SETUP_FAILED = 7
    """
    Error setting up audio channel. Since 1.10.
    """
    MM_CALL_STATE_REASON_TRANSFERRED = 8
    """
    Call has been transferred. Since 1.12.
    """
    MM_CALL_STATE_REASON_DEFLECTED = 9
    """
    Call has been deflected to a new number. Since 1.12.
    """


class MMFirmwareImageType(Enum):
    """
    Type of firmware image.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_FIRMWARE_IMAGE_TYPE_UNKNOWN = 0
    """
    Unknown firmware type.
    """
    MM_FIRMWARE_IMAGE_TYPE_GENERIC = 1
    """
    Generic firmware image.
    """
    MM_FIRMWARE_IMAGE_TYPE_GOBI = 2
    """
    Firmware image of Gobi devices.
    """


class MMModem3gppFacility(Enum):
    """
    A bitfield describing which facilities have a lock enabled, i.e., requires a pin or unlock code. The facilities include the personalizations (device locks) described in 3GPP spec TS 22.022, and the PIN and PIN2 locks, which are SIM locks.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_3GPP_FACILITY_NONE = 0
    """
    No facility.
    """
    MM_MODEM_3GPP_FACILITY_SIM = 1
    """
    SIM lock.
    """
    MM_MODEM_3GPP_FACILITY_FIXED_DIALING = 2
    """
    Fixed dialing (PIN2) SIM lock.
    """
    MM_MODEM_3GPP_FACILITY_PH_SIM = 3
    """
    Device is locked to a specific SIM.
    """
    MM_MODEM_3GPP_FACILITY_PH_FSIM = 4
    """
    Device is locked to first SIM inserted.
    """
    MM_MODEM_3GPP_FACILITY_NET_PERS = 5
    """
    Network personalization.
    """
    MM_MODEM_3GPP_FACILITY_NET_SUB_PERS = 6
    """
    Network subset personalization.
    """
    MM_MODEM_3GPP_FACILITY_PROVIDER_PERS = 7
    """
    Service provider personalization.
    """
    MM_MODEM_3GPP_FACILITY_CORP_PERS = 8
    """
    Corporate personalization.
    """


class MMModem3gppNetworkAvailability(Enum):
    """
    Network availability status as defined in 3GPP TS 27.007 section 7.3.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_3GPP_NETWORK_AVAILABILITY_UNKNOWN = 0
    """
    Unknown availability.
    """
    MM_MODEM_3GPP_NETWORK_AVAILABILITY_AVAILABLE = 1
    """
    Network is available.
    """
    MM_MODEM_3GPP_NETWORK_AVAILABILITY_CURRENT = 2
    """
    Network is the current one.
    """
    MM_MODEM_3GPP_NETWORK_AVAILABILITY_FORBIDDEN = 3
    """
    Network is forbidden.
    """


class MMModem3gppSubscriptionState(Enum):
    """
    Describes the current subscription status of the SIM. This value is only available after the modem attempts to register with the network.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_3GPP_SUBSCRIPTION_STATE_UNKNOWN = 0
    """
    The subscription state is unknown.
    """
    MM_MODEM_3GPP_SUBSCRIPTION_STATE_UNPROVISIONED = 1
    """
    The account is unprovisioned.
    """
    MM_MODEM_3GPP_SUBSCRIPTION_STATE_PROVISIONED = 2
    """
    The account is provisioned and has data available.
    """
    MM_MODEM_3GPP_SUBSCRIPTION_STATE_OUT_OF_DATA = 3
    """
    The account is provisioned but there is no data left.
    """


class MMModem3gppRegistrationState(Enum):
    """
    GSM registration code as defined in 3GPP TS 27.007.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_IDLE = 0
    """
    Not registered, not searching for new operator to register.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_HOME = 1
    """
    Registered on home network.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_SEARCHING = 2
    """
    Not registered, searching for new operator to register with.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_DENIED = 3
    """
    Registration denied.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_UNKNOWN = 4
    """
    Unknown registration status.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING = 5
    """
    Registered on a roaming network.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_HOME_SMS_ONLY = 6
    """
    Registered for "SMS only", home network (applicable only when on LTE). Since 1.8.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING_SMS_ONLY = 7
    """
    Registered for "SMS only", roaming network (applicable only when on LTE). Since 1.8.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_EMERGENCY_ONLY = 8
    """
    Emergency services only. Since 1.8.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_HOME_CSFB_NOT_PREFERRED = 9
    """
    Registered for "CSFB not preferred", home network (applicable only when on LTE). Since 1.8.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING_CSFB_NOT_PREFERRED = 10
    """
    Registered for "CSFB not preferred", roaming network (applicable only when on LTE). Since 1.8.
    """
    MM_MODEM_3GPP_REGISTRATION_STATE_ATTACHED_RLOS = 11
    """
    Attached for access to Restricted Local Operator Services (applicable only when on LTE). Since 1.14.
    """


class MMModem3gppUssdSessionState(Enum):
    """
    State of a USSD session.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_3GPP_USSD_SESSION_STATE_UNKNOWN = 0
    """
    Unknown state.
    """
    MM_MODEM_3GPP_USSD_SESSION_STATE_IDLE = 1
    """
    No active session.
    """
    MM_MODEM_3GPP_USSD_SESSION_STATE_ACTIVE = 2
    """
    A session is active and the mobile is waiting for a response.
    """
    MM_MODEM_3GPP_USSD_SESSION_STATE_USER_RESPONSE = 3
    """
    The network is waiting for the client's response.
    """


class MMModem3gppEpsUeModeOperation(Enum):
    """
    UE mode of operation for EPS, as per 3GPP TS 24.301.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_3GPP_EPS_UE_MODE_OPERATION_UNKNOWN = 0
    """
    Unknown or not applicable.
    """
    MM_MODEM_3GPP_EPS_UE_MODE_OPERATION_PS_1 = 1
    """
    PS mode 1 of operation: EPS only, voice-centric.
    """
    MM_MODEM_3GPP_EPS_UE_MODE_OPERATION_PS_2 = 2
    """
    PS mode 2 of operation: EPS only, data-centric.
    """
    MM_MODEM_3GPP_EPS_UE_MODE_OPERATION_CSPS_1 = 3
    """
    CS/PS mode 1 of operation: EPS and non-EPS, voice-centric.
    """
    MM_MODEM_3GPP_EPS_UE_MODE_OPERATION_CSPS_2 = 4
    """
    CS/PS mode 2 of operation: EPS and non-EPS, data-centric.
    """


class MMModemAccessTechnology(Enum):
    """
    Describes various access technologies that a device uses when registered with or connected to a network.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_ACCESS_TECHNOLOGY_UNKNOWN = 0
    """
    The access technology used is unknown.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_POTS = 1
    """
    Analog wireline telephone.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_GSM = 2
    """
    GSM.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT = 3
    """
    Compact GSM.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_GPRS = 4
    """
    GPRS.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_EDGE = 5
    """
    EDGE (ETSI 27.007: "GSM w/EGPRS").
    """
    MM_MODEM_ACCESS_TECHNOLOGY_UMTS = 6
    """
    UMTS (ETSI 27.007: "UTRAN").
    """
    MM_MODEM_ACCESS_TECHNOLOGY_HSDPA = 7
    """
    HSDPA (ETSI 27.007: "UTRAN w/HSDPA").
    """
    MM_MODEM_ACCESS_TECHNOLOGY_HSUPA = 8
    """
    HSUPA (ETSI 27.007: "UTRAN w/HSUPA").
    """
    MM_MODEM_ACCESS_TECHNOLOGY_HSPA = 9
    """
    HSPA (ETSI 27.007: "UTRAN w/HSDPA and HSUPA").
    """
    MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS = 10
    """
    HSPA+ (ETSI 27.007: "UTRAN w/HSPA+").
    """
    MM_MODEM_ACCESS_TECHNOLOGY_1XRTT = 11
    """
    CDMA2000 1xRTT.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_EVDO0 = 12
    """
    CDMA2000 EVDO revision 0.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_EVDOA = 13
    """
    CDMA2000 EVDO revision A.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_EVDOB = 14
    """
    CDMA2000 EVDO revision B.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_LTE = 15
    """
    LTE (ETSI 27.007: "E-UTRAN")
    """
    MM_MODEM_ACCESS_TECHNOLOGY_5GNR = 16
    """
    5GNR (ETSI 27.007: "NG-RAN"). Since 1.14.
    """
    MM_MODEM_ACCESS_TECHNOLOGY_ANY = 17
    """
    Mask specifying all access technologies.
    """


class MMModemBand(Enum):
    """
    Radio bands supported by the device when connecting to a mobile network.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_BAND_UNKNOWN = 0
    """
    Unknown or invalid band.
    """
    MM_MODEM_BAND_EGSM = 1
    """
    GSM/GPRS/EDGE 900 MHz.
    """
    MM_MODEM_BAND_DCS = 2
    """
    GSM/GPRS/EDGE 1800 MHz.
    """
    MM_MODEM_BAND_PCS = 3
    """
    GSM/GPRS/EDGE 1900 MHz.
    """
    MM_MODEM_BAND_G850 = 4
    """
    GSM/GPRS/EDGE 850 MHz.
    """
    MM_MODEM_BAND_UTRAN_1 = 5
    """
    UMTS 2100 MHz (IMT, UTRAN band 1). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_3 = 6
    """
    UMTS 1800 MHz (DCS, UTRAN band 3). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_4 = 7
    """
    UMTS 1700 MHz (AWS A-F, UTRAN band 4). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_6 = 8
    """
    UMTS 800 MHz (UTRAN band 6). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_5 = 9
    """
    UMTS 850 MHz (CLR, UTRAN band 5). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_8 = 10
    """
    UMTS 900 MHz (E-GSM, UTRAN band 8). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_9 = 11
    """
    UMTS 1700 MHz (UTRAN band 9). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_2 = 12
    """
    UMTS 1900 MHz (PCS A-F, UTRAN band 2). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_7 = 13
    """
    UMTS 2600 MHz (IMT-E, UTRAN band 7). Since 1.8.
    """
    MM_MODEM_BAND_G450 = 14
    """
    GSM/GPRS/EDGE 450 MHz.
    """
    MM_MODEM_BAND_G480 = 15
    """
    GSM/GPRS/EDGE 480 MHz.
    """
    MM_MODEM_BAND_G750 = 16
    """
    GSM/GPRS/EDGE 750 MHz.
    """
    MM_MODEM_BAND_G380 = 17
    """
    GSM/GPRS/EDGE 380 MHz.
    """
    MM_MODEM_BAND_G410 = 18
    """
    GSM/GPRS/EDGE 410 MHz.
    """
    MM_MODEM_BAND_G710 = 19
    """
    GSM/GPRS/EDGE 710 MHz.
    """
    MM_MODEM_BAND_G810 = 20
    """
    GSM/GPRS/EDGE 810 MHz.
    """
    MM_MODEM_BAND_EUTRAN_1 = 21
    """
    E-UTRAN band 1. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_2 = 22
    """
    E-UTRAN band 2. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_3 = 23
    """
    E-UTRAN band 3. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_4 = 24
    """
    E-UTRAN band 4. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_5 = 25
    """
    E-UTRAN band 5. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_6 = 26
    """
    E-UTRAN band 6. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_7 = 27
    """
    E-UTRAN band 7. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_8 = 28
    """
    E-UTRAN band 8. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_9 = 29
    """
    E-UTRAN band 9. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_10 = 30
    """
    E-UTRAN band 10. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_11 = 31
    """
    E-UTRAN band 11. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_12 = 32
    """
    E-UTRAN band 12. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_13 = 33
    """
    E-UTRAN band 13. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_14 = 34
    """
    E-UTRAN band 14. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_17 = 35
    """
    E-UTRAN band 17. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_18 = 36
    """
    E-UTRAN band 18. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_19 = 37
    """
    E-UTRAN band 19. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_20 = 38
    """
    E-UTRAN band 20. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_21 = 39
    """
    E-UTRAN band 21. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_22 = 40
    """
    E-UTRAN band 22. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_23 = 41
    """
    E-UTRAN band 23. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_24 = 42
    """
    E-UTRAN band 24. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_25 = 43
    """
    E-UTRAN band 25. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_26 = 44
    """
    E-UTRAN band 26. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_27 = 45
    """
    E-UTRAN band 27. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_28 = 46
    """
    E-UTRAN band 28. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_29 = 47
    """
    E-UTRAN band 29. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_30 = 48
    """
    E-UTRAN band 30. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_31 = 49
    """
    E-UTRAN band 31. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_32 = 50
    """
    E-UTRAN band 32. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_33 = 51
    """
    E-UTRAN band 33. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_34 = 52
    """
    E-UTRAN band 34. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_35 = 53
    """
    E-UTRAN band 35. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_36 = 54
    """
    E-UTRAN band 36. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_37 = 55
    """
    E-UTRAN band 37. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_38 = 56
    """
    E-UTRAN band 38. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_39 = 57
    """
    E-UTRAN band 39. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_40 = 58
    """
    E-UTRAN band 40. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_41 = 59
    """
    E-UTRAN band 41. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_42 = 60
    """
    E-UTRAN band 42. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_43 = 61
    """
    E-UTRAN band 43. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_44 = 62
    """
    E-UTRAN band 44. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_45 = 63
    """
    E-UTRAN band 45. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_46 = 64
    """
    E-UTRAN band 46. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_47 = 65
    """
    E-UTRAN band 47. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_48 = 66
    """
    E-UTRAN band 48. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_49 = 67
    """
    E-UTRAN band 49. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_50 = 68
    """
    E-UTRAN band 50. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_51 = 69
    """
    E-UTRAN band 51. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_52 = 70
    """
    E-UTRAN band 52. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_53 = 71
    """
    E-UTRAN band 53. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_54 = 72
    """
    E-UTRAN band 54. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_55 = 73
    """
    E-UTRAN band 55. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_56 = 74
    """
    E-UTRAN band 56. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_57 = 75
    """
    E-UTRAN band 57. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_58 = 76
    """
    E-UTRAN band 58. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_59 = 77
    """
    E-UTRAN band 59. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_60 = 78
    """
    E-UTRAN band 60. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_61 = 79
    """
    E-UTRAN band 61. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_62 = 80
    """
    E-UTRAN band 62. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_63 = 81
    """
    E-UTRAN band 63. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_64 = 82
    """
    E-UTRAN band 64. Since 1.10.
    """
    MM_MODEM_BAND_EUTRAN_65 = 83
    """
    E-UTRAN band 65. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_66 = 84
    """
    E-UTRAN band 66. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_67 = 85
    """
    E-UTRAN band 67. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_68 = 86
    """
    E-UTRAN band 68. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_69 = 87
    """
    E-UTRAN band 69. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_70 = 88
    """
    E-UTRAN band 70. Since 1.8.
    """
    MM_MODEM_BAND_EUTRAN_71 = 89
    """
    E-UTRAN band 71. Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC0 = 90
    """
    CDMA Band Class 0 (US Cellular 850MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC1 = 91
    """
    CDMA Band Class 1 (US PCS 1900MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC2 = 92
    """
    CDMA Band Class 2 (UK TACS 900MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC3 = 93
    """
    CDMA Band Class 3 (Japanese TACS). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC4 = 94
    """
    CDMA Band Class 4 (Korean PCS). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC5 = 95
    """
    CDMA Band Class 5 (NMT 450MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC6 = 96
    """
    CDMA Band Class 6 (IMT2000 2100MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC7 = 97
    """
    CDMA Band Class 7 (Cellular 700MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC8 = 98
    """
    CDMA Band Class 8 (1800MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC9 = 99
    """
    CDMA Band Class 9 (900MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC10 = 100
    """
    CDMA Band Class 10 (US Secondary 800). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC11 = 101
    """
    CDMA Band Class 11 (European PAMR 400MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC12 = 102
    """
    CDMA Band Class 12 (PAMR 800MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC13 = 103
    """
    CDMA Band Class 13 (IMT2000 2500MHz Expansion). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC14 = 104
    """
    CDMA Band Class 14 (More US PCS 1900MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC15 = 105
    """
    CDMA Band Class 15 (AWS 1700MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC16 = 106
    """
    CDMA Band Class 16 (US 2500MHz). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC17 = 107
    """
    CDMA Band Class 17 (US 2500MHz Forward Link Only). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC18 = 108
    """
    CDMA Band Class 18 (US 700MHz Public Safety). Since 1.8.
    """
    MM_MODEM_BAND_CDMA_BC19 = 109
    """
    CDMA Band Class 19 (US Lower 700MHz). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_10 = 110
    """
    UMTS 1700 MHz (EAWS A-G, UTRAN band 10). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_11 = 111
    """
    UMTS 1500 MHz (LPDC, UTRAN band 11). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_12 = 112
    """
    UMTS 700 MHz (LSMH A/B/C, UTRAN band 12). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_13 = 113
    """
    UMTS 700 MHz (USMH C, UTRAN band 13). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_14 = 114
    """
    UMTS 700 MHz (USMH D, UTRAN band 14). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_19 = 115
    """
    UMTS 800 MHz (UTRAN band 19). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_20 = 116
    """
    UMTS 800 MHz (EUDD, UTRAN band 20). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_21 = 117
    """
    UMTS 1500 MHz (UPDC, UTRAN band 21). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_22 = 118
    """
    UMTS 3500 MHz (UTRAN band 22). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_25 = 119
    """
    UMTS 1900 MHz (EPCS A-G, UTRAN band 25). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_26 = 120
    """
    UMTS 850 MHz (ECLR, UTRAN band 26). Since 1.8.
    """
    MM_MODEM_BAND_UTRAN_32 = 121
    """
    UMTS 1500 MHz (L-band, UTRAN band 32). Since 1.8.
    """
    MM_MODEM_BAND_ANY = 122
    """
    For certain operations, allow the modem to select a band automatically.
    """


class MMModemCapability(Enum):
    """
    Flags describing one or more of the general access technology families that a modem supports.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_CAPABILITY_NONE = 0
    """
    Modem has no capabilities.
    """
    MM_MODEM_CAPABILITY_POTS = 1
    """
    Modem supports the analog wired telephone network (ie 56k dialup) and does not have wireless/cellular capabilities.
    """
    MM_MODEM_CAPABILITY_CDMA_EVDO = 2
    """
    Modem supports at least one of CDMA 1xRTT, EVDO revision 0, EVDO revision A, or EVDO revision B.
    """
    MM_MODEM_CAPABILITY_GSM_UMTS = 3
    """
    Modem supports at least one of GSM, GPRS, EDGE, UMTS, HSDPA, HSUPA, or HSPA+ packet switched data capability.
    """
    MM_MODEM_CAPABILITY_LTE = 4
    """
    Modem has LTE data capability.
    """
    MM_MODEM_CAPABILITY_IRIDIUM = 5
    """
    Modem has Iridium capabilities.
    """
    MM_MODEM_CAPABILITY_5GNR = 6
    """
    Modem has 5GNR capabilities. Since 1.14.
    """
    MM_MODEM_CAPABILITY_ANY = 7
    """
    Mask specifying all capabilities.
    """


class MMModemCdmaActivationState(Enum):
    """
    Activation state of a CDMA modem.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_CDMA_ACTIVATION_STATE_UNKNOWN = 0
    """
    Unknown activation state.
    """
    MM_MODEM_CDMA_ACTIVATION_STATE_NOT_ACTIVATED = 1
    """
    Device is not activated
    """
    MM_MODEM_CDMA_ACTIVATION_STATE_ACTIVATING = 2
    """
    Device is activating
    """
    MM_MODEM_CDMA_ACTIVATION_STATE_PARTIALLY_ACTIVATED = 3
    """
    Device is partially activated; carrier-specific steps required to continue.
    """
    MM_MODEM_CDMA_ACTIVATION_STATE_ACTIVATED = 4
    """
    Device is ready for use.
    """


class MMModemCdmaRegistrationState(Enum):
    """
    Registration state of a CDMA modem.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_CDMA_REGISTRATION_STATE_UNKNOWN = 0
    """
    Registration status is unknown or the device is not registered.
    """
    MM_MODEM_CDMA_REGISTRATION_STATE_REGISTERED = 1
    """
    Registered, but roaming status is unknown or cannot be provided by the device. The device may or may not be roaming.
    """
    MM_MODEM_CDMA_REGISTRATION_STATE_HOME = 2
    """
    Currently registered on the home network.
    """
    MM_MODEM_CDMA_REGISTRATION_STATE_ROAMING = 3
    """
    Currently registered on a roaming network.
    """


class MMModemCdmaRmProtocol(Enum):
    """
    Protocol of the Rm interface in modems with CDMA capabilities.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_CDMA_RM_PROTOCOL_UNKNOWN = 0
    """
    Unknown protocol.
    """
    MM_MODEM_CDMA_RM_PROTOCOL_ASYNC = 1
    """
    Asynchronous data or fax.
    """
    MM_MODEM_CDMA_RM_PROTOCOL_PACKET_RELAY = 2
    """
    Packet data service, Relay Layer Rm interface.
    """
    MM_MODEM_CDMA_RM_PROTOCOL_PACKET_NETWORK_PPP = 3
    """
    Packet data service, Network Layer Rm interface, PPP.
    """
    MM_MODEM_CDMA_RM_PROTOCOL_PACKET_NETWORK_SLIP = 4
    """
    Packet data service, Network Layer Rm interface, SLIP.
    """
    MM_MODEM_CDMA_RM_PROTOCOL_STU_III = 5
    """
    STU-III service.
    """


class MMModemContactsStorage(Enum):
    """
    Specifies different storage locations for contact information.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_CONTACTS_STORAGE_UNKNOWN = 0
    """
    Unknown location.
    """
    MM_MODEM_CONTACTS_STORAGE_ME = 1
    """
    Device's local memory.
    """
    MM_MODEM_CONTACTS_STORAGE_SM = 2
    """
    Card inserted in the device (like a SIM/RUIM).
    """
    MM_MODEM_CONTACTS_STORAGE_MT = 3
    """
    Combined device/ME and SIM/SM phonebook.
    """


class MMModemLocationSource(Enum):
    """
    Sources of location information supported by the modem.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_LOCATION_SOURCE_NONE = 0
    """
    None.
    """
    MM_MODEM_LOCATION_SOURCE_3GPP_LAC_CI = 1
    """
    Location Area Code and Cell ID.
    """
    MM_MODEM_LOCATION_SOURCE_GPS_RAW = 2
    """
    GPS location given by predefined keys.
    """
    MM_MODEM_LOCATION_SOURCE_GPS_NMEA = 3
    """
    GPS location given as NMEA traces.
    """
    MM_MODEM_LOCATION_SOURCE_CDMA_BS = 4
    """
    CDMA base station position.
    """
    MM_MODEM_LOCATION_SOURCE_GPS_UNMANAGED = 5
    """
    No location given, just GPS module setup. Since 1.4.
    """
    MM_MODEM_LOCATION_SOURCE_AGPS_MSA = 6
    """
    Mobile Station Assisted A-GPS location requested. Since 1.12.
    """
    MM_MODEM_LOCATION_SOURCE_AGPS_MSB = 7
    """
    Mobile Station Based A-GPS location requested. Since 1.12.
    """


class MMModemLocationAssistanceDataType(Enum):
    """
    Type of assistance data that may be injected to the GNSS module.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_LOCATION_ASSISTANCE_DATA_TYPE_NONE = 0
    """
    None.
    """
    MM_MODEM_LOCATION_ASSISTANCE_DATA_TYPE_XTRA = 1
    """
    Qualcomm gpsOneXTRA.
    """


class MMModemLock(Enum):
    """
    Enumeration of possible lock reasons.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_LOCK_UNKNOWN = 0
    """
    Lock reason unknown.
    """
    MM_MODEM_LOCK_NONE = 1
    """
    Modem is unlocked.
    """
    MM_MODEM_LOCK_SIM_PIN = 2
    """
    SIM requires the PIN code.
    """
    MM_MODEM_LOCK_SIM_PIN2 = 3
    """
    SIM requires the PIN2 code.
    """
    MM_MODEM_LOCK_SIM_PUK = 4
    """
    SIM requires the PUK code.
    """
    MM_MODEM_LOCK_SIM_PUK2 = 5
    """
    SIM requires the PUK2 code.
    """
    MM_MODEM_LOCK_PH_SP_PIN = 6
    """
    Modem requires the service provider PIN code.
    """
    MM_MODEM_LOCK_PH_SP_PUK = 7
    """
    Modem requires the service provider PUK code.
    """
    MM_MODEM_LOCK_PH_NET_PIN = 8
    """
    Modem requires the network PIN code.
    """
    MM_MODEM_LOCK_PH_NET_PUK = 9
    """
    Modem requires the network PUK code.
    """
    MM_MODEM_LOCK_PH_SIM_PIN = 10
    """
    Modem requires the PIN code.
    """
    MM_MODEM_LOCK_PH_CORP_PIN = 11
    """
    Modem requires the corporate PIN code.
    """
    MM_MODEM_LOCK_PH_CORP_PUK = 12
    """
    Modem requires the corporate PUK code.
    """
    MM_MODEM_LOCK_PH_FSIM_PIN = 13
    """
    Modem requires the PH-FSIM PIN code.
    """
    MM_MODEM_LOCK_PH_FSIM_PUK = 14
    """
    Modem requires the PH-FSIM PUK code.
    """
    MM_MODEM_LOCK_PH_NETSUB_PIN = 15
    """
    Modem requires the network subset PIN code.
    """
    MM_MODEM_LOCK_PH_NETSUB_PUK = 16
    """
    Modem requires the network subset PUK code.
    """


class MMModemMode(Enum):
    """
    Bitfield to indicate which access modes are supported, allowed or preferred in a given device.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_MODE_NONE = 0
    """
    None.
    """
    MM_MODEM_MODE_CS = 1
    """
    CSD, GSM, and other circuit-switched technologies.
    """
    MM_MODEM_MODE_2G = 2
    """
    GPRS, EDGE.
    """
    MM_MODEM_MODE_3G = 3
    """
    UMTS, HSxPA.
    """
    MM_MODEM_MODE_4G = 4
    """
    LTE.
    """
    MM_MODEM_MODE_5G = 5
    """
    5GNR. Since 1.14.
    """
    MM_MODEM_MODE_ANY = 6
    """
    Any mode can be used (only this value allowed for POTS modems).
    """


class MMModemState(Enum):
    """
    Enumeration of possible modem states.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_STATE_FAILED = 0
    """
    The modem is unusable.
    """
    MM_MODEM_STATE_UNKNOWN = 1
    """
    State unknown or not reportable.
    """
    MM_MODEM_STATE_INITIALIZING = 2
    """
    The modem is currently being initialized.
    """
    MM_MODEM_STATE_LOCKED = 3
    """
    The modem needs to be unlocked.
    """
    MM_MODEM_STATE_DISABLED = 4
    """
    The modem is not enabled and is powered down.
    """
    MM_MODEM_STATE_DISABLING = 5
    """
    The modem is currently transitioning to the MM_MODEM_STATE_DISABLED state.
    """
    MM_MODEM_STATE_ENABLING = 6
    """
    The modem is currently transitioning to the MM_MODEM_STATE_ENABLED state.
    """
    MM_MODEM_STATE_ENABLED = 7
    """
    The modem is enabled and powered on but not registered with a network provider and not available for data connections.
    """
    MM_MODEM_STATE_SEARCHING = 8
    """
    The modem is searching for a network provider to register with.
    """
    MM_MODEM_STATE_REGISTERED = 9
    """
    The modem is registered with a network provider, and data connections and messaging may be available for use.
    """
    MM_MODEM_STATE_DISCONNECTING = 10
    """
    The modem is disconnecting and deactivating the last active packet data bearer. This state will not be entered if more than one packet data bearer is active and one of the active bearers is deactivated.
    """
    MM_MODEM_STATE_CONNECTING = 11
    """
    The modem is activating and connecting the first packet data bearer. Subsequent bearer activations when another bearer is already active do not cause this state to be entered.
    """
    MM_MODEM_STATE_CONNECTED = 12
    """
    One or more packet data bearers is active and connected.
    """


class MMModemStateFailedReason(Enum):
    """
    Enumeration of possible errors when the modem is in MM_MODEM_STATE_FAILED .

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_STATE_FAILED_REASON_NONE = 0
    """
    No error.
    """
    MM_MODEM_STATE_FAILED_REASON_UNKNOWN = 1
    """
    Unknown error.
    """
    MM_MODEM_STATE_FAILED_REASON_SIM_MISSING = 2
    """
    SIM is required but missing.
    """
    MM_MODEM_STATE_FAILED_REASON_SIM_ERROR = 3
    """
    SIM is available, but unusable (e.g. permanently locked).
    """


class MMModemStateChangeReason(Enum):
    """
    Enumeration of possible reasons to have changed the modem state.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_STATE_CHANGE_REASON_UNKNOWN = 0
    """
    Reason unknown or not reportable.
    """
    MM_MODEM_STATE_CHANGE_REASON_USER_REQUESTED = 1
    """
    State change was requested by an interface user.
    """
    MM_MODEM_STATE_CHANGE_REASON_SUSPEND = 2
    """
    State change was caused by a system suspend.
    """
    MM_MODEM_STATE_CHANGE_REASON_FAILURE = 3
    """
    State change was caused by an unrecoverable error.
    """


class MMModemPowerState(Enum):
    """
    Power state of the modem.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_POWER_STATE_UNKNOWN = 0
    """
    Unknown power state.
    """
    MM_MODEM_POWER_STATE_OFF = 1
    """
    Off.
    """
    MM_MODEM_POWER_STATE_LOW = 2
    """
    Low-power mode.
    """
    MM_MODEM_POWER_STATE_ON = 3
    """
    Full power mode.
    """


class MMModemPortType(Enum):
    """
    Type of modem port.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_PORT_TYPE_UNKNOWN = 0
    """
    Unknown.
    """
    MM_MODEM_PORT_TYPE_NET = 1
    """
    Net port.
    """
    MM_MODEM_PORT_TYPE_AT = 2
    """
    AT port.
    """
    MM_MODEM_PORT_TYPE_QCDM = 3
    """
    QCDM port.
    """
    MM_MODEM_PORT_TYPE_GPS = 4
    """
    GPS port.
    """
    MM_MODEM_PORT_TYPE_QMI = 5
    """
    QMI port.
    """
    MM_MODEM_PORT_TYPE_MBIM = 6
    """
    MBIM port.
    """
    MM_MODEM_PORT_TYPE_AUDIO = 7
    """
    Audio port. Since 1.12.
    """
    MM_MODEM_PORT_TYPE_IGNORED = 8
    """
    Ignored port. Since 1.16.
    """


class MMModemFirmwareUpdateMethod(Enum):
    """
    Type of firmware update method supported by the module.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_MODEM_FIRMWARE_UPDATE_METHOD_NONE = 0
    """
    No method specified.
    """
    MM_MODEM_FIRMWARE_UPDATE_METHOD_FASTBOOT = 1
    """
    Device supports fastboot-based update.
    """
    MM_MODEM_FIRMWARE_UPDATE_METHOD_QMI_PDC = 2
    """
    Device supports QMI PDC based update.
    """
    MM_MODEM_FIRMWARE_UPDATE_METHOD_MBIM_QDU = 3
    """
    Device supports MBIM QDU based update. Since 1.18.
    """
    MM_MODEM_FIRMWARE_UPDATE_METHOD_FIREHOSE = 4
    """
    Device supports Firehose based update. Since 1.18.
    """


class MMOmaFeature(Enum):
    """
    Features that can be enabled or disabled in the OMA device management support.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_OMA_FEATURE_NONE = 0
    """
    None.
    """
    MM_OMA_FEATURE_DEVICE_PROVISIONING = 1
    """
    Device provisioning service.
    """
    MM_OMA_FEATURE_PRL_UPDATE = 2
    """
    PRL update service.
    """
    MM_OMA_FEATURE_HANDS_FREE_ACTIVATION = 3
    """
    Hands free activation service.
    """


class MMOmaSessionState(Enum):
    """
    State of the OMA device management session.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_OMA_SESSION_STATE_FAILED = 0
    """
    Failed.
    """
    MM_OMA_SESSION_STATE_UNKNOWN = 1
    """
    Unknown.
    """
    MM_OMA_SESSION_STATE_STARTED = 2
    """
    Started.
    """
    MM_OMA_SESSION_STATE_RETRYING = 3
    """
    Retrying.
    """
    MM_OMA_SESSION_STATE_CONNECTING = 4
    """
    Connecting.
    """
    MM_OMA_SESSION_STATE_CONNECTED = 5
    """
    Connected.
    """
    MM_OMA_SESSION_STATE_AUTHENTICATED = 6
    """
    Authenticated.
    """
    MM_OMA_SESSION_STATE_MDN_DOWNLOADED = 7
    """
    MDN downloaded.
    """
    MM_OMA_SESSION_STATE_MSID_DOWNLOADED = 8
    """
    MSID downloaded.
    """
    MM_OMA_SESSION_STATE_PRL_DOWNLOADED = 9
    """
    PRL downloaded.
    """
    MM_OMA_SESSION_STATE_MIP_PROFILE_DOWNLOADED = 10
    """
    MIP profile downloaded.
    """
    MM_OMA_SESSION_STATE_COMPLETED = 11
    """
    Session completed.
    """


class MMOmaSessionStateFailedReason(Enum):
    """
    Reason of failure in the OMA device management session.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_OMA_SESSION_STATE_FAILED_REASON_UNKNOWN = 0
    """
    No reason or unknown.
    """
    MM_OMA_SESSION_STATE_FAILED_REASON_NETWORK_UNAVAILABLE = 1
    """
    Network unavailable.
    """
    MM_OMA_SESSION_STATE_FAILED_REASON_SERVER_UNAVAILABLE = 2
    """
    Server unavailable.
    """
    MM_OMA_SESSION_STATE_FAILED_REASON_AUTHENTICATION_FAILED = 3
    """
    Authentication failed.
    """
    MM_OMA_SESSION_STATE_FAILED_REASON_MAX_RETRY_EXCEEDED = 4
    """
    Maximum retries exceeded.
    """
    MM_OMA_SESSION_STATE_FAILED_REASON_SESSION_CANCELLED = 5
    """
    Session cancelled.
    """


class MMOmaSessionType(Enum):
    """
    Type of OMA device management session.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_OMA_SESSION_TYPE_UNKNOWN = 0
    """
    Unknown session type.
    """
    MM_OMA_SESSION_TYPE_CLIENT_INITIATED_DEVICE_CONFIGURE = 1
    """
    Client-initiated device configure.
    """
    MM_OMA_SESSION_TYPE_CLIENT_INITIATED_PRL_UPDATE = 2
    """
    Client-initiated PRL update.
    """
    MM_OMA_SESSION_TYPE_CLIENT_INITIATED_HANDS_FREE_ACTIVATION = 3
    """
    Client-initiated hands free activation.
    """
    MM_OMA_SESSION_TYPE_NETWORK_INITIATED_DEVICE_CONFIGURE = 4
    """
    Network-initiated device configure.
    """
    MM_OMA_SESSION_TYPE_NETWORK_INITIATED_PRL_UPDATE = 5
    """
    Network-initiated PRL update.
    """
    MM_OMA_SESSION_TYPE_DEVICE_INITIATED_PRL_UPDATE = 6
    """
    Device-initiated PRL update.
    """
    MM_OMA_SESSION_TYPE_DEVICE_INITIATED_HANDS_FREE_ACTIVATION = 7
    """
    Device-initiated hands free activation.
    """


class MMSmsPduType(Enum):
    """
    Type of PDUs used in the SMS.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_PDU_TYPE_UNKNOWN = 0
    """
    Unknown type.
    """
    MM_SMS_PDU_TYPE_DELIVER = 1
    """
    3GPP Mobile-Terminated (MT) message.
    """
    MM_SMS_PDU_TYPE_SUBMIT = 2
    """
    3GPP Mobile-Originated (MO) message.
    """
    MM_SMS_PDU_TYPE_STATUS_REPORT = 3
    """
    3GPP status report (MT).
    """
    MM_SMS_PDU_TYPE_CDMA_DELIVER = 4
    """
    3GPP2 Mobile-Terminated (MT) message. Since 1.2.
    """
    MM_SMS_PDU_TYPE_CDMA_SUBMIT = 5
    """
    3GPP2 Mobile-Originated (MO) message. Since 1.2.
    """
    MM_SMS_PDU_TYPE_CDMA_CANCELLATION = 6
    """
    3GPP2 Cancellation (MO) message. Since 1.2.
    """
    MM_SMS_PDU_TYPE_CDMA_DELIVERY_ACKNOWLEDGEMENT = 7
    """
    3GPP2 Delivery Acknowledgement (MT) message. Since 1.2.
    """
    MM_SMS_PDU_TYPE_CDMA_USER_ACKNOWLEDGEMENT = 8
    """
    3GPP2 User Acknowledgement (MT or MO) message. Since 1.2.
    """
    MM_SMS_PDU_TYPE_CDMA_READ_ACKNOWLEDGEMENT = 9
    """
    3GPP2 Read Acknowledgement (MT or MO) message. Since 1.2.
    """


class MMSmsState(Enum):
    """
    State of a given SMS.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_STATE_UNKNOWN = 0
    """
    State unknown or not reportable.
    """
    MM_SMS_STATE_STORED = 1
    """
    The message has been neither received nor yet sent.
    """
    MM_SMS_STATE_RECEIVING = 2
    """
    The message is being received but is not yet complete.
    """
    MM_SMS_STATE_RECEIVED = 3
    """
    The message has been completely received.
    """
    MM_SMS_STATE_SENDING = 4
    """
    The message is queued for delivery.
    """
    MM_SMS_STATE_SENT = 5
    """
    The message was successfully sent.
    """


class MMSmsDeliveryState(Enum):
    """
    Enumeration of known SMS delivery states as defined in 3GPP TS 03.40 and 3GPP2 N.S0005-O, section 6.5.2.125.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_DELIVERY_STATE_COMPLETED_RECEIVED = 0
    """
    Delivery completed, message received by the SME.
    """
    MM_SMS_DELIVERY_STATE_COMPLETED_FORWARDED_UNCONFIRMED = 1
    """
    Forwarded by the SC to the SME but the SC is unable to confirm delivery.
    """
    MM_SMS_DELIVERY_STATE_COMPLETED_REPLACED_BY_SC = 2
    """
    Message replaced by the SC.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_CONGESTION = 3
    """
    Temporary error, congestion.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_SME_BUSY = 4
    """
    Temporary error, SME busy.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_NO_RESPONSE_FROM_SME = 5
    """
    Temporary error, no response from the SME.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_SERVICE_REJECTED = 6
    """
    Temporary error, service rejected.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_QOS_NOT_AVAILABLE = 7
    """
    Temporary error, QoS not available.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_IN_SME = 8
    """
    Temporary error in the SME.
    """
    MM_SMS_DELIVERY_STATE_ERROR_REMOTE_PROCEDURE = 9
    """
    Permanent remote procedure error.
    """
    MM_SMS_DELIVERY_STATE_ERROR_INCOMPATIBLE_DESTINATION = 10
    """
    Permanent error, incompatible destination.
    """
    MM_SMS_DELIVERY_STATE_ERROR_CONNECTION_REJECTED = 11
    """
    Permanent error, connection rejected by the SME.
    """
    MM_SMS_DELIVERY_STATE_ERROR_NOT_OBTAINABLE = 12
    """
    Permanent error, not obtainable.
    """
    MM_SMS_DELIVERY_STATE_ERROR_QOS_NOT_AVAILABLE = 13
    """
    Permanent error, QoS not available.
    """
    MM_SMS_DELIVERY_STATE_ERROR_NO_INTERWORKING_AVAILABLE = 14
    """
    Permanent error, no interworking available.
    """
    MM_SMS_DELIVERY_STATE_ERROR_VALIDITY_PERIOD_EXPIRED = 15
    """
    Permanent error, message validity period expired.
    """
    MM_SMS_DELIVERY_STATE_ERROR_DELETED_BY_ORIGINATING_SME = 16
    """
    Permanent error, deleted by originating SME.
    """
    MM_SMS_DELIVERY_STATE_ERROR_DELETED_BY_SC_ADMINISTRATION = 17
    """
    Permanent error, deleted by SC administration.
    """
    MM_SMS_DELIVERY_STATE_ERROR_MESSAGE_DOES_NOT_EXIST = 18
    """
    Permanent error, message does no longer exist.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_CONGESTION = 19
    """
    Permanent error, congestion.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_SME_BUSY = 20
    """
    Permanent error, SME busy.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_NO_RESPONSE_FROM_SME = 21
    """
    Permanent error, no response from the SME.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_SERVICE_REJECTED = 22
    """
    Permanent error, service rejected.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_QOS_NOT_AVAILABLE = 23
    """
    Permanent error, QoS not available.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_IN_SME = 24
    """
    Permanent error in SME.
    """
    MM_SMS_DELIVERY_STATE_UNKNOWN = 25
    """
    Unknown state.
    """
    MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_ADDRESS_VACANT = 26
    """
    Permanent error in network, address vacant. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE = 27
    """
    Permanent error in network, address translation failure. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE = 28
    """
    Permanent error in network, network resource outage. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_NETWORK_FAILURE = 29
    """
    Permanent error in network, network failure. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_INVALID_TELESERVICE_ID = 30
    """
    Permanent error in network, invalid teleservice id. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_OTHER = 31
    """
    Permanent error, other network problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_NO_PAGE_RESPONSE = 32
    """
    Permanent error in terminal, no page response. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_BUSY = 33
    """
    Permanent error in terminal, destination busy. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT = 34
    """
    Permanent error in terminal, no acknowledgement. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE = 35
    """
    Permanent error in terminal, destination resource shortage. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED = 36
    """
    Permanent error in terminal, SMS delivery postponed. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE = 37
    """
    Permanent error in terminal, destination out of service. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS = 38
    """
    Permanent error in terminal, destination no longer at this address. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_OTHER = 39
    """
    Permanent error, other terminal problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE = 40
    """
    Permanent error in radio interface, resource shortage. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY = 41
    """
    Permanent error in radio interface, problem incompatibility. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_OTHER = 42
    """
    Permanent error, other radio interface problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_ENCODING = 43
    """
    Permanent error, encoding. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED = 44
    """
    Permanent error, SMS origination denied. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_TERMINATION_DENIED = 45
    """
    Permanent error, SMS termination denied. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED = 46
    """
    Permanent error, supplementary service not supported. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_NOT_SUPPORTED = 47
    """
    Permanent error, SMS not supported. Since 1.22.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER = 48
    """
    Permanent error, missing expected parameter. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER = 49
    """
    Permanent error, missing mandatory parameter. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE = 50
    """
    Permanent error, unrecognized parameter value. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE = 51
    """
    Permanent error, unexpected parameter value. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR = 52
    """
    Permanent error, user data size error. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_OTHER = 53
    """
    Permanent error, other general problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_ADDRESS_VACANT = 54
    """
    Temporary error in network, address vacant. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE = 55
    """
    Temporary error in network, address translation failure. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE = 56
    """
    Temporary error in network, network resource outage. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_NETWORK_FAILURE = 57
    """
    Temporary error in network, network failure. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_INVALID_TELESERVICE_ID = 58
    """
    Temporary error in network, invalid teleservice id. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_OTHER = 59
    """
    Temporary error, other network problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_NO_PAGE_RESPONSE = 60
    """
    Temporary error in terminal, no page response. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_BUSY = 61
    """
    Temporary error in terminal, destination busy. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT = 62
    """
    Temporary error in terminal, no acknowledgement. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE = 63
    """
    Temporary error in terminal, destination resource shortage. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED = 64
    """
    Temporary error in terminal, SMS delivery postponed. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE = 65
    """
    Temporary error in terminal, destination out of service. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS = 66
    """
    Temporary error in terminal, destination no longer at this address. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_OTHER = 67
    """
    Temporary error, other terminal problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE = 68
    """
    Temporary error in radio interface, resource shortage. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY = 69
    """
    Temporary error in radio interface, problem incompatibility. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_OTHER = 70
    """
    Temporary error, other radio interface problem. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_ENCODING = 71
    """
    Temporary error, encoding. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED = 72
    """
    Temporary error, SMS origination denied. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_TERMINATION_DENIED = 73
    """
    Temporary error, SMS termination denied. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED = 74
    """
    Temporary error, supplementary service not supported. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_NOT_SUPPORTED = 75
    """
    Temporary error, SMS not supported. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER = 76
    """
    Temporary error, missing expected parameter. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER = 77
    """
    Temporary error, missing mandatory parameter. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE = 78
    """
    Temporary error, unrecognized parameter value. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE = 79
    """
    Temporary error, unexpected parameter value. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR = 80
    """
    Temporary error, user data size error. Since 1.2.
    """
    MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_OTHER = 81
    """
    Temporary error, other general problem. Since 1.2.
    """


class MMSmsStorage(Enum):
    """
    Storage for SMS messages.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_STORAGE_UNKNOWN = 0
    """
    Storage unknown.
    """
    MM_SMS_STORAGE_SM = 1
    """
    SIM card storage area.
    """
    MM_SMS_STORAGE_ME = 2
    """
    Mobile equipment storage area.
    """
    MM_SMS_STORAGE_MT = 3
    """
    Sum of SIM and Mobile equipment storages
    """
    MM_SMS_STORAGE_SR = 4
    """
    Status report message storage area.
    """
    MM_SMS_STORAGE_BM = 5
    """
    Broadcast message storage area.
    """
    MM_SMS_STORAGE_TA = 6
    """
    Terminal adaptor message storage area.
    """


class MMSmsValidityType(Enum):
    """
    Type of SMS validity value.

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_VALIDITY_TYPE_UNKNOWN = 0
    """
    Validity type unknown.
    """
    MM_SMS_VALIDITY_TYPE_RELATIVE = 1
    """
    Relative validity.
    """
    MM_SMS_VALIDITY_TYPE_ABSOLUTE = 2
    """
    Absolute validity.
    """
    MM_SMS_VALIDITY_TYPE_ENHANCED = 3
    """
    Enhanced validity.
    """


class MMSmsCdmaTeleserviceId(Enum):
    """
    Teleservice IDs supported for CDMA SMS, as defined in 3GPP2 X.S0004-550-E (section 2.256) and 3GPP2 C.S0015-B (section 3.4.3.1).

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_CDMA_TELESERVICE_ID_UNKNOWN = 0
    """
    Unknown.
    """
    MM_SMS_CDMA_TELESERVICE_ID_CMT91 = 1
    """
    IS-91 Extended Protocol Enhanced Services.
    """
    MM_SMS_CDMA_TELESERVICE_ID_WPT = 2
    """
    Wireless Paging Teleservice.
    """
    MM_SMS_CDMA_TELESERVICE_ID_WMT = 3
    """
    Wireless Messaging Teleservice.
    """
    MM_SMS_CDMA_TELESERVICE_ID_VMN = 4
    """
    Voice Mail Notification.
    """
    MM_SMS_CDMA_TELESERVICE_ID_WAP = 5
    """
    Wireless Application Protocol.
    """
    MM_SMS_CDMA_TELESERVICE_ID_WEMT = 6
    """
    Wireless Enhanced Messaging Teleservice.
    """
    MM_SMS_CDMA_TELESERVICE_ID_SCPT = 7
    """
    Service Category Programming Teleservice.
    """
    MM_SMS_CDMA_TELESERVICE_ID_CATPT = 8
    """
    Card Application Toolkit Protocol Teleservice.
    """


class MMSmsCdmaServiceCategory(Enum):
    """
    Service category for CDMA SMS, as defined in 3GPP2 C.R1001-D (section 9.3).

    Since: `1.10 <https://www.freedesktop.org/software/ModemManager/doc/latest/ModemManager/api-index-1-10.html#api-index-1.10>`_
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_UNKNOWN = 0
    """
    Unknown.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_EMERGENCY_BROADCAST = 1
    """
    Emergency broadcast.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_ADMINISTRATIVE = 2
    """
    Administrative.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_MAINTENANCE = 3
    """
    Maintenance.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_LOCAL = 4
    """
    General news (local).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_REGIONAL = 5
    """
    General news (regional).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_NATIONAL = 6
    """
    General news (national).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_INTERNATIONAL = 7
    """
    General news (international).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_LOCAL = 8
    """
    Business/Financial news (local).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_REGIONAL = 9
    """
    Business/Financial news (regional).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_NATIONAL = 10
    """
    Business/Financial news (national).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_INTERNATIONAL = 11
    """
    Business/Financial news (international).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_LOCAL = 12
    """
    Sports news (local).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_REGIONAL = 13
    """
    Sports news (regional).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_NATIONAL = 14
    """
    Sports news (national).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_INTERNATIONAL = 15
    """
    Sports news (international).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_LOCAL = 16
    """
    Entertainment news (local).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_REGIONAL = 17
    """
    Entertainment news (regional).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_NATIONAL = 18
    """
    Entertainment news (national).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_INTERNATIONAL = 19
    """
    Entertainment news (international).
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_LOCAL_WEATHER = 20
    """
    Local weather.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_TRAFFIC_REPORT = 21
    """
    Area traffic report.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_FLIGHT_SCHEDULES = 22
    """
    Local airport flight schedules.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_RESTAURANTS = 23
    """
    Restaurants.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_LODGINGS = 24
    """
    Lodgings.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_RETAIL_DIRECTORY = 25
    """
    Retail directory.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_ADVERTISEMENTS = 26
    """
    Advertisements.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_STOCK_QUOTES = 27
    """
    Stock quotes.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_EMPLOYMENT = 28
    """
    Employment.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_HOSPITALS = 29
    """
    Medical / Health / Hospitals.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_TECHNOLOGY_NEWS = 30
    """
    Technology news.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_MULTICATEGORY = 31
    """
    Multi-category.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_PRESIDENTIAL_ALERT = 32
    """
    Presidential alert.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_EXTREME_THREAT = 33
    """
    Extreme threat.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_SEVERE_THREAT = 34
    """
    Severe threat.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_CHILD_ABDUCTION_EMERGENCY = 35
    """
    Child abduction emergency.
    """
    MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_TEST = 36
    """
    CMAS test.
    """
