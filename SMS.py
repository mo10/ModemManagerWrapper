from typing import Tuple

from ModemManagerWrapper.MMInterface import MMInterface
from ModemManagerWrapper.ModemManager import ModemManager
from MMEnum import MMSmsState, MMSmsPduType, MMSmsCdmaTeleserviceId, MMSmsCdmaServiceCategory, MMSmsDeliveryState, \
    MMSmsStorage, MMSmsValidityType


class SMS(MMInterface):
    """
    The SMS interface Defines operations and properties of a single SMS message.
    """

    def __init__(self, manager: ModemManager, instance):
        super().__init__(manager)
        self._instance = instance

    def Send(self):
        """
        If the message has not yet been sent, queue it for delivery.

        Since: 1.0
        """
        self._instance.Send()

    def Store(self, storage: MMSmsStorage):
        """
        Store the message in the device if not already done.

        This method requires a MMSmsStorage value, describing the storage where this message is to be kept;
        or MM_SMS_STORAGE_UNKNOWN if the default storage should be used.

        Since: 1.0
        """
        self._instance.Store(storage.value)

    @property
    def State(self) -> MMSmsState:
        """
        A MMSmsState value, describing the state of the message.

        Since: 1.0
        :return: MMSmsState
        """
        return MMSmsState(self._instance.State)

    @property
    def PduType(self) -> MMSmsPduType:
        """
        A MMSmsPduType value, describing the type of PDUs used in the SMS message.

        Since: 1.0
        :return: MMSmsPduType
        """
        return MMSmsPduType(self._instance.PduType)

    @property
    def Number(self) -> str:
        """
        Number to which the message is addressed.

        Since: 1.0
        :return: string
        """
        return self._instance.Number

    @property
    def Text(self) -> str:
        """
        Message text, in UTF-8.

        When sending, if the text is larger than the limit of the technology or modem,
        the message will be broken into multiple parts or messages.

        Note that Text and Data are never given at the same time.

        Since: 1.0
        :return: string
        """
        return self._instance.Text

    @property
    def Data(self) -> bytes:
        """
        Message data.

        When sending, if the data is larger than the limit of the technology or modem,
        the message will be broken into multiple parts or messages.

        Note that Text and Data are never given at the same time.

        Since: 1.0
        :return: bytes
        """
        return bytes(self._instance.Data)

    @property
    def SMSC(self) -> str:
        """
        Indicates the SMS service center number.

        Always empty for 3GPP2/CDMA.

        Since: 1.0
        :return: string
        """
        return self._instance.SMSC

    @property
    def Validity(self) -> Tuple[MMSmsValidityType, int]:
        """
        Indicates when the SMS expires in the SMSC.

        This value is composed of a MMSmsValidityType key,
        with an associated data which contains type-specific validity information:

            MM_SMS_VALIDITY_TYPE_RELATIVEL:
                The value is the length of the validity period in minutes,
                given as an unsigned integer (D-Bus signature 'u').

        Since: 1.0
        :return: int
        """
        key, value = self._instance.Validity
        key = MMSmsValidityType(key)
        value = int(value)
        return key, value

    @property
    def Class(self) -> int:
        """
        3GPP message class (-1..3).

        -1 means class is not available or is not used for this message,
        otherwise the 3GPP SMS message class.

        Always -1 for 3GPP2/CDMA.

        Since: 1.0
        :return: int
        """
        return self._instance.Class

    @property
    def TeleserviceId(self) -> MMSmsCdmaTeleserviceId:
        """
        A MMSmsCdmaTeleserviceId value.

        Always MM_SMS_CDMA_TELESERVICE_ID_UNKNOWN for 3GPP.

        Since: 1.2
        :return: MMSmsCdmaTeleserviceId
        """
        return MMSmsCdmaTeleserviceId(self._instance.TeleserviceId)

    @property
    def ServiceCategory(self) -> MMSmsCdmaServiceCategory:
        """
        A MMSmsCdmaServiceCategory value.

        Always MM_SMS_CDMA_SERVICE_CATEGORY_UNKNOWN for 3GPP.

        Since: 1.2
        :return: MMSmsCdmaServiceCategory
        """
        return MMSmsCdmaServiceCategory(self._instance.ServiceCategory)

    @property
    def DeliveryReportRequest(self) -> bool:
        """
        #TRUE if delivery report request is required, #FALSE otherwise.

        Since: 1.0
        :return: bool
        """
        return self._instance.DeliveryReportRequest

    @property
    def MessageReference(self) -> int:
        """
        Message Reference of the last PDU sent/received within this SMS.

        If the PDU type is MM_SMS_PDU_TYPE_STATUS_REPORT,
        this field identifies the Message Reference of the PDU associated to the status report.

        Since: 1.0
        :return: int
        """
        return self._instance.MessageReference

    @property
    def Timestamp(self) -> str:
        """
        Time when the first PDU of the SMS message arrived the SMSC, in ISO8601 format.
        This field is only applicable if the PDU type is MM_SMS_PDU_TYPE_DELIVER. or MM_SMS_PDU_TYPE_STATUS_REPORT.

        Since: 1.0
        :return: string
        """
        return self._instance.Timestamp

    @property
    def DischargeTimestamp(self) -> str:
        """
        Time when the first PDU of the SMS message left the SMSC, in ISO8601 format.

        This field is only applicable if the PDU type is MM_SMS_PDU_TYPE_STATUS_REPORT.

        Since: 1.0
        :return: string
        """
        return self._instance.DischargeTimestamp

    @property
    def DeliveryState(self) -> MMSmsDeliveryState:
        """
        A MMSmsDeliveryState value, describing the state of the delivery reported in the Status Report message.

        This field is only applicable if the PDU type is MM_SMS_PDU_TYPE_STATUS_REPORT.

        Since: 1.0
        :return: MMSmsDeliveryState
        """
        return MMSmsDeliveryState(self._instance.DeliveryState)

    @property
    def Storage(self) -> MMSmsStorage:
        """
        A MMSmsStorage value, describing the storage where this message is kept.

        Since: 1.0
        :return: MMSmsDeliveryState
        """
        return MMSmsStorage(self._instance.Storage)
