---
Description: 'Defines the PKEYs associated with PnP-X providers.'
ms.assetid: 'd297705b-d825-4aa5-8269-ef44bc5875d7'
title: 'PnP-X Provider PKEYs'
---

# PnP-X Provider PKEYs

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

A PnP-X provider is a type of built-in provider. The [SSDP](ssdp-provider.md) and [WSD](wsd-provider.md) providers implement the PnP-X provider type and the PnP-X PKEYs, in addition to implementing protocol-specific functionality and PKEYs. The values associated with the properties named below are supplied by the device in metadata messages.

<dl> <dt>

<span id="PKEY_PNPX_GlobalIdentity"></span><span id="pkey_pnpx_globalidentity"></span><span id="PKEY_PNPX_GLOBALIDENTITY"></span>**PKEY\_PNPX\_GlobalIdentity**
</dt> <dd> <dl> <dt>



The UUID of the root device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Types"></span><span id="pkey_pnpx_types"></span><span id="PKEY_PNPX_TYPES"></span>**PKEY\_PNPX\_Types**
</dt> <dd> <dl> <dt>



The types of messages sent or received, as described in the device's discovery message. PROPVARIANT type VT\_VECTOR \| VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Scopes"></span><span id="pkey_pnpx_scopes"></span><span id="PKEY_PNPX_SCOPES"></span>**PKEY\_PNPX\_Scopes**
</dt> <dd> <dl> <dt>



The discoverable groups of network endpoints providing services to the device. PROPVARIANT type VT\_VECTOR \| VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_XAddrs"></span><span id="pkey_pnpx_xaddrs"></span><span id="PKEY_PNPX_XADDRS"></span>**PKEY\_PNPX\_XAddrs**
</dt> <dd> <dl> <dt>



A list of XAddrs provided in the [Hello](https://msdn.microsoft.com/library/windows/desktop/bb513682), [ProbeMatch](https://msdn.microsoft.com/library/windows/desktop/bb513683), or [ResolveMatch](https://msdn.microsoft.com/library/windows/desktop/bb513685) messages sent by the device. PROPVARIANT type VT\_VECTOR \| VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_MetadataVersion"></span><span id="pkey_pnpx_metadataversion"></span><span id="PKEY_PNPX_METADATAVERSION"></span>**PKEY\_PNPX\_MetadataVersion**
</dt> <dd> <dl> <dt>



The metadata version. This is a non-negative integer that is incremented on metadata change. Metadata includes types and scopes. PROPVARIANT type VT\_UI8.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ID"></span><span id="pkey_pnpx_id"></span>**PKEY\_PNPX\_ID**
</dt> <dd> <dl> <dt>



The unique identifier of the device. For root devices, this property has the same value as PKEY\_PNPX\_GlobalIdentity. PROPVARIANT type VT\_LPWSTR.

> [!Note]  
> Devices cannot share an identifier, even if the devices use different protocols. If a device implements more than one protocol, the device must have a unique identifier for each protocol.

 


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_RemoteAddress"></span><span id="pkey_pnpx_remoteaddress"></span><span id="PKEY_PNPX_REMOTEADDRESS"></span>**PKEY\_PNPX\_RemoteAddress**
</dt> <dd> <dl> <dt>



The remote address of the device. The address is only populated by the WSD provider when the device is discovered by directed discovery. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Manufacturer"></span><span id="pkey_pnpx_manufacturer"></span><span id="PKEY_PNPX_MANUFACTURER"></span>**PKEY\_PNPX\_Manufacturer**
</dt> <dd> <dl> <dt>



A human-readable form of the name of the device manufacturer. This string can be localized. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ManufacturerUrl"></span><span id="pkey_pnpx_manufacturerurl"></span><span id="PKEY_PNPX_MANUFACTURERURL"></span>**PKEY\_PNPX\_ManufacturerUrl**
</dt> <dd> <dl> <dt>



The URL of the device manufacturer's web site. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ModelName"></span><span id="pkey_pnpx_modelname"></span><span id="PKEY_PNPX_MODELNAME"></span>**PKEY\_PNPX\_ModelName**
</dt> <dd> <dl> <dt>



A human-readable form of the model name of the device. This string can be localized. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ModelNumber"></span><span id="pkey_pnpx_modelnumber"></span><span id="PKEY_PNPX_MODELNUMBER"></span>**PKEY\_PNPX\_ModelNumber**
</dt> <dd> <dl> <dt>



A human-readable form of the model number of the device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ModelUrl"></span><span id="pkey_pnpx_modelurl"></span><span id="PKEY_PNPX_MODELURL"></span>**PKEY\_PNPX\_ModelUrl**
</dt> <dd> <dl> <dt>



The URL of the page containing the description of the device model. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Upc"></span><span id="pkey_pnpx_upc"></span><span id="PKEY_PNPX_UPC"></span>**PKEY\_PNPX\_Upc**
</dt> <dd> <dl> <dt>



A human-readable form of the device product code. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_PresentationUrl"></span><span id="pkey_pnpx_presentationurl"></span><span id="PKEY_PNPX_PRESENTATIONURL"></span>**PKEY\_PNPX\_PresentationUrl**
</dt> <dd> <dl> <dt>



The presentation URL for a web page that controls the device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_FriendlyName"></span><span id="pkey_pnpx_friendlyname"></span><span id="PKEY_PNPX_FRIENDLYNAME"></span>**PKEY\_PNPX\_FriendlyName**
</dt> <dd> <dl> <dt>



The display name for the device. This string can be localized. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_FirmwareVersion"></span><span id="pkey_pnpx_firmwareversion"></span><span id="PKEY_PNPX_FIRMWAREVERSION"></span>**PKEY\_PNPX\_FirmwareVersion**
</dt> <dd> <dl> <dt>



The firmware version for this device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_SerialNumber"></span><span id="pkey_pnpx_serialnumber"></span><span id="PKEY_PNPX_SERIALNUMBER"></span>**PKEY\_PNPX\_SerialNumber**
</dt> <dd> <dl> <dt>



A human-readable form of the serial number of the device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_DeviceCategory"></span><span id="pkey_pnpx_devicecategory"></span><span id="PKEY_PNPX_DEVICECATEGORY"></span>**PKEY\_PNPX\_DeviceCategory**
</dt> <dd> <dl> <dt>



The device category. PnP-X categories are the namespaces in which components that provide similar base functionality are grouped.

Each category has predefined keywords associated with it. These keywords are used to restrict the list of devices displayed in the **Network Explorer**. When the user types one of the predefined keywords into the **Search Category** box, **Network Explorer** displays only the items in the matching category.

Some categories have predefined subcategories. A subcategory can be specified in the device metadata, and its value will be stored in the PKEY\_PNPX\_DeviceCategory property key instead of the parent category value.

Subcategories are not displayed in the **Network Explorer**. Instead, a subcategory's parent category value is displayed. Subcategories can be queried programmatically, but they cannot be queried by the end-user.

Providers can define and use their own subcategories, but they cannot define their own categories.

The following table shows the possible device categories.



| Name                                           | Value                    | Description                                                                                                                                                                                                                                                                                      |
|------------------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PNPX\_DEVICECATEGORY\_COMPUTER                 | L"Computers"             | **Computers** category.Keywords: Computer, Laptop, Tablet<br/> Defined subcategories: Computers.PC, Computers.MediaCenter, Computers.Server<br/>                                                                                                                                     |
| PNPX\_DEVICECATEGORY\_INPUTDEVICE              | L"Input"                 | **Input Devices** category.Keywords: Keyboard, Mouse, Input<br/> Defined subcategories: Input.Keyboard, Input.Mouse<br/>                                                                                                                                                             |
| PNPX\_DEVICECATEGORY\_PRINTER                  | L"Printers"              | **Printers** category.Keyword: Printer<br/>                                                                                                                                                                                                                                                |
| PNPX\_DEVICECATEGORY\_SCANNER                  | L"Scanners"              | **Scanners** category.Keyword: Scanner<br/>                                                                                                                                                                                                                                                |
| PNPX\_DEVICECATEGORY\_FAX                      | L"FAX"                   | **FAX** category.Keyword: FAX<br/>                                                                                                                                                                                                                                                         |
| PNPX\_DEVICECATEGORY\_MFP                      | L"MFP"                   | **Multifunction Devices** category.Keywords: Multifunction Device, MFP<br/>                                                                                                                                                                                                                |
| PNPX\_DEVICECATEGORY\_CAMERA                   | L"Cameras"               | **Cameras** category.Keywords: Camera, Video Camera, Digital Camera<br/> Defined subcategories: Cameras.DigitalStillCamera, Cameras.VideoCamera<br/>                                                                                                                                 |
| PNPX\_DEVICECATEGORY\_STORAGE                  | L"Storage"               | **Storage** category.Keywords: Hard Drive, CD, CD-ROM, DVD, DVD-ROM, Flash, SD<br/> Defined subcategory: Storage.NAS<br/>                                                                                                                                                            |
| PNPX\_DEVICECATEGORY\_NETWORK\_INFRASTRUCTURE  | L"NetworkInfrastructure" | **Network Infrastructure** category.Keywords: Hub, Switch, Gateway, Router, Access Point, Modem<br/> Defined subcategories: NetworkInfrastructure.AccessPoint, NetworkInfrastructure.Router, NetworkInfrastructure.Switch<br/>                                                       |
| PNPX\_DEVICECATEGORY\_DISPLAYS                 | L"Displays"              | **Displays** category.Keywords: Monitor, Projector, Television, Digital Picture Frame<br/> Defined subcategory: Displays.Monitor<br/>                                                                                                                                                |
| PNPX\_DEVICECATEGORY\_MULTIMEDIA\_DEVICE       | L"MediaDevices"          | **Media Devices** category.Keywords: Music Player, Music Server, MP3 Player, WMA Player, Pika, Media Extender, Stereo, A/V Receiver, Cable, Satellite, DVR, Speakers<br/> Defined subcategories: MediaDevices.DVR, MediaDevices.DAR, MediaDevices.MCE, MediaDevices.MusicPlayer<br/> |
| PNPX\_DEVICECATEGORY\_GAMING\_DEVICE           | L"Gaming"                | **Gaming Devices** category.Keywords: Xbox, Controller, Joystick<br/> Defined subcategories: Gaming.Xbox, Gaming.Xbox360<br/>                                                                                                                                                        |
| PNPX\_DEVICECATEGORY\_TELEPHONE                | L"Phones"                | **Phones** category.Keywords: Telephone, Cell Phone, Pager<br/> Defined subcategories: Phones.CellPhone, Phones.WindowsMobile<br/>                                                                                                                                                   |
| PNPX\_DEVICECATEGORY\_HOME\_AUTOMATION\_SYSTEM | L"HomeAutomation"        | **Home Automation** category.Keywords: Light, Thermostat, Heater, A/C, Air Conditioning<br/> Defined subcategories: HomeAutomation.Light, HomeAutomation.Thermostat, HomeAutomation.Heater, HomeAutomation.AC<br/>                                                                   |
| PNPX\_DEVICECATEGORY\_HOME\_SECURITY\_SYSTEM   | L"HomeSecurity"          | **Home Security** category.Keywords: Security, Home Security<br/>                                                                                                                                                                                                                          |
| PNPX\_DEVICECATEGORY\_OTHER                    | L"Other"                 | **Other Devices** category.There are no keywords or subcategories associated with this category.<br/>                                                                                                                                                                                      |



 

PROPVARIANT type VT\_LPWSTR \| VT\_VECTOR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_DeviceCategory_Desc"></span><span id="pkey_pnpx_devicecategory_desc"></span><span id="PKEY_PNPX_DEVICECATEGORY_DESC"></span>**PKEY\_PNPX\_DeviceCategory\_Desc**
</dt> <dd> <dl> <dt>



The category description. PROPVARIANT type VT\_LPWSTR \| VT\_VECTOR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_PhysicalAddress"></span><span id="pkey_pnpx_physicaladdress"></span><span id="PKEY_PNPX_PHYSICALADDRESS"></span>**PKEY\_PNPX\_PhysicalAddress**
</dt> <dd> <dl> <dt>



The physical address of the device on the network interface. PROPVARIANT type VT\_UI1 \| VT\_VECTOR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_NetworkInterfaceLuid"></span><span id="pkey_pnpx_networkinterfaceluid"></span><span id="PKEY_PNPX_NETWORKINTERFACELUID"></span>**PKEY\_PNPX\_NetworkInterfaceLuid**
</dt> <dd> <dl> <dt>



The LUID of the network interface upon which the device was discovered. PROPVARIANT type VT\_UI8.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_NetworkInterfaceGuid"></span><span id="pkey_pnpx_networkinterfaceguid"></span><span id="PKEY_PNPX_NETWORKINTERFACEGUID"></span>**PKEY\_PNPX\_NetworkInterfaceGuid**
</dt> <dd> <dl> <dt>



The GUID of the network interface upon which the device was discovered. PROPVARIANT type VT\_CLSID.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_IpAddress"></span><span id="pkey_pnpx_ipaddress"></span><span id="PKEY_PNPX_IPADDRESS"></span>**PKEY\_PNPX\_IpAddress**
</dt> <dd> <dl> <dt>



The IP address of the device. PROPVARIANT type VT\_LPWSTR \| VT\_VECTOR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ServiceAddress"></span><span id="pkey_pnpx_serviceaddress"></span><span id="PKEY_PNPX_SERVICEADDRESS"></span>**PKEY\_PNPX\_ServiceAddress**
</dt> <dd> <dl> <dt>



The address of a [*hosted service*](function-discovery-glossary.md#hosted-service-ncd-gly). The service information is derived from the relationship metadata provided by the device. PROPVARIANT type VT\_LPWSTR \| VT\_VECTOR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ServiceId"></span><span id="pkey_pnpx_serviceid"></span><span id="PKEY_PNPX_SERVICEID"></span>**PKEY\_PNPX\_ServiceId**
</dt> <dd> <dl> <dt>



An identifier for a hosted service. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ServiceTypes"></span><span id="pkey_pnpx_servicetypes"></span><span id="PKEY_PNPX_SERVICETYPES"></span>**PKEY\_PNPX\_ServiceTypes**
</dt> <dd> <dl> <dt>



The types of messages sent and received by a hosted service. PROPVARIANT type VT\_LPWSTR \| VT\_VECTOR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Devnode"></span><span id="pkey_pnpx_devnode"></span><span id="PKEY_PNPX_DEVNODE"></span>**PKEY\_PNPX\_Devnode**
</dt> <dd> <dl> <dt>



The [*devnode*](function-discovery-glossary.md#devnode-ncd-gly). PROPVARIANT type VT\_BOOL.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_AssociationState"></span><span id="pkey_pnpx_associationstate"></span><span id="PKEY_PNPX_ASSOCIATIONSTATE"></span>**PKEY\_PNPX\_AssociationState**
</dt> <dd> <dl> <dt>



Specifies whether the device is associated with a computer. PROPVARIANT type VT\_UINT.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_AssociatedInstanceId"></span><span id="pkey_pnpx_associatedinstanceid"></span><span id="PKEY_PNPX_ASSOCIATEDINSTANCEID"></span>**PKEY\_PNPX\_AssociatedInstanceId**
</dt> <dd> <dl> <dt>



Specifies the instance identifier of the device associated with the computer. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_LastNotificationTime"></span><span id="pkey_pnpx_lastnotificationtime"></span><span id="PKEY_PNPX_LASTNOTIFICATIONTIME"></span>**PKEY\_PNPX\_LastNotificationTime**
</dt> <dd> <dl> <dt>



The most recent time that the PnP-X service IP bus enumerator (IPBusEnum) saw or connected to a device. PROPVARIANT type VT\_DATE.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_DomainName"></span><span id="pkey_pnpx_domainname"></span><span id="PKEY_PNPX_DOMAINNAME"></span>**PKEY\_PNPX\_DomainName**
</dt> <dd> <dl> <dt>



Specifies the domain name of the network to which the device is connected. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_ShareName"></span><span id="pkey_pnpx_sharename"></span><span id="PKEY_PNPX_SHARENAME"></span>**PKEY\_PNPX\_ShareName**
</dt> <dd> <dl> <dt>



The share name. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Installable"></span><span id="pkey_pnpx_installable"></span><span id="PKEY_PNPX_INSTALLABLE"></span>**PKEY\_PNPX\_Installable**
</dt> <dd> <dl> <dt>



Specifies that the device can be installed using the user interface. A device is installable if a **hardwareID** or **compatibleID** is specified in the device description document. PROPVARIANT type VT\_BOOL.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_Installed"></span><span id="pkey_pnpx_installed"></span><span id="PKEY_PNPX_INSTALLED"></span>**PKEY\_PNPX\_Installed**
</dt> <dd> <dl> <dt>



Specifies the installation state (installed or not installed). PROPVARIANT type VT\_BOOL.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_CompatibleTypes"></span><span id="pkey_pnpx_compatibletypes"></span><span id="PKEY_PNPX_COMPATIBLETYPES"></span>**PKEY\_PNPX\_CompatibleTypes**
</dt> <dd> <dl> <dt>



Specifies the types of devices with which the PnP-X device is compatible. This PKEY may contain several values, listed in order from the most specific to the least specific device type.

If **PKEY\_PNPX\_Installable** is VARIANT\_TRUE, the PKEY\_PNPX\_CompatibleTypes key is populated with the list of hardware identifiers and compatible identifiers provided by the device. The hardware identifiers precede the compatible identifiers in the identifier list.

If **PKEY\_PNPX\_Installable** is VARIANT\_FALSE, the PKEY\_PNPX\_CompatibleTypes key is populated with the following for SSDP devices:

-   manufacturer + "/" + modelName + "/" modelNumber
-   manufacturer + "/" + modelName
-   deviceType

If **PKEY\_PNPX\_Installable** is VARIANT\_FALSE, the PKEY\_PNPX\_CompatibleTypes key is populated with the following for WSD devices:

-   wsd:ThisModel/wsd:manufacturer + "/" + wsd:ThisModel/wsd:modelName + "/" + wsd:ThisModel/wsd:modelNumber
-   wsd:ThisModel/wsd:manufacturer + "/" + wsd:ThisModel/wsd:modelName
-   wsdisco:Types

PROPVARIANT type VT\_VECTOR \| VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_SecureChannel"></span><span id="pkey_pnpx_securechannel"></span><span id="PKEY_PNPX_SECURECHANNEL"></span>**PKEY\_PNPX\_SecureChannel**
</dt> <dd> <dl> <dt>



Specifies whether the device uses HTTPS for metadata exchange and service messaging. PROPVARIANT type VT\_BOOL.


</dt> </dl> </dd> <dt>

<span id="PKEY_PNPX_CompactSignature"></span><span id="pkey_pnpx_compactsignature"></span><span id="PKEY_PNPX_COMPACTSIGNATURE"></span>**PKEY\_PNPX\_CompactSignature**
</dt> <dd> <dl> <dt>



Specifies whether the device uses HTTPS for metadata exchange and service messaging and signs discovery messages using the compact signature format. PROPVARIANT type VT\_BOOL.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryKeys.h</dt> </dl> |



## See also

<dl> <dt>

[**Key Definitions**](key-definitions.md)
</dt> </dl>

 

 




