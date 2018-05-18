---
Description: 'Defines the PKEYs associated with the Windows Connect Now (WCN) Provider.'
ms.assetid: '5667022d-7893-4456-bfdb-7ffe08a68520'
title: WCN Provider PKEYs
---

# WCN Provider PKEYs

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The following keys are associated with the Windows Connect Now (WCN) provider.

<dl> <dt>

<span id="PKEY_WCN_AssocState"></span><span id="pkey_wcn_assocstate"></span><span id="PKEY_WCN_ASSOCSTATE"></span>**PKEY\_WCN\_AssocState**
</dt> <dd> <dl> <dt>



The configuration and association state of the wireless station when sending a Discovery request.

The following table shows the possible configuration and association states.



| Association State | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| 0                 | Not associated.                                                   |
| 1                 | The connection was successfully established.                      |
| 2                 | Configuration failed.                                             |
| 3                 | Association failed.                                               |
| 4                 | Connection failed. Could not connect to the specified IP address. |



 

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_AuthType"></span><span id="pkey_wcn_authtype"></span><span id="PKEY_WCN_AUTHTYPE"></span>**PKEY\_WCN\_AuthType**
</dt> <dd> <dl> <dt>



The network authentication capabilities of the enrollee. An enrollee is an association point (AP) or station.

The following table shows the authentication types and associated values.



| Authentication Type | Value  | Required/Optional |
|---------------------|--------|-------------------|
| Open                | 0x0001 | Required.         |
| WPAPSK              | 0x0002 | Required.         |
| Shared              | 0x0004 | Required.         |
| WPA                 | 0x0008 | Required.         |
| WPA2                | 0x0010 | Optional.         |
| WPA2PSK             | 0x0020 | Optional.         |



 

An enrollee must support the required authentication types, and may support the optional authentication types. To determine the value associated with the **PKEY\_WCN\_AuthType** key for an enrollee, combine the values associated with the supported authentication types using the bitwise OR operator.

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_ConfigError"></span><span id="pkey_wcn_configerror"></span><span id="PKEY_WCN_CONFIGERROR"></span>**PKEY\_WCN\_ConfigError**
</dt> <dd> <dl> <dt>



The result of a device's configuration and association attempt.

The following table shows the possible error results.



| Error Value | Description                                                      |
|-------------|------------------------------------------------------------------|
| 0           | No error.                                                        |
| 1           | Could not read the out-of-band (OOB) interface.                  |
| 2           | Could not decrypt the Cyclic Redundancy Check (CRC) value.       |
| 3           | The 2.4 GHz channel is not supported.                            |
| 4           | The 5.0 GHz channel is not supported.                            |
| 5           | The signal is too weak.                                          |
| 6           | Network authentication failed.                                   |
| 7           | Network association failed.                                      |
| 8           | The DHCP server did not respond.                                 |
| 9           | DHCP configuration failed.                                       |
| 10          | There was an IP address conflict.                                |
| 11          | Could not connect to the registrar.                              |
| 12          | Multiple push button configuration (PBC) sessions were detected. |
| 13          | Rogue activity is suspected.                                     |
| 14          | The device is busy.                                              |
| 15          | Setup is locked.                                                 |
| 16          | The message timed out.                                           |
| 17          | The registration session timed out.                              |
| 18          | Device password authentication failed.                           |



 

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_ConfigMethods"></span><span id="pkey_wcn_configmethods"></span><span id="PKEY_WCN_CONFIGMETHODS"></span>**PKEY\_WCN\_ConfigMethods**
</dt> <dd> <dl> <dt>



The configuration methods supported by the enrollee or registrar.

The following table shows the possible configuration methods.



| Value  | Hardware Interface Used For Configuration     |
|--------|-----------------------------------------------|
| 0x0001 | USB-A (flash drive)                           |
| 0x0002 | Ethernet                                      |
| 0x0004 | Label                                         |
| 0x0008 | Display                                       |
| 0x0010 | External near-field communication (NFC) token |
| 0x0020 | Integrated NFC token                          |
| 0x0040 | NFC interface                                 |
| 0x0080 | Push button                                   |
| 0x0100 | Keypad                                        |



 

An enrollee or registrar must support one or more of the above configuration methods. To determine the value associated with the **PKEY\_WCN\_ConfigMethods** key for an enrollee or registrar, combine the values associated with the supported configuration methods using the bitwise OR operator.

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_ConfigState"></span><span id="pkey_wcn_configstate"></span><span id="PKEY_WCN_CONFIGSTATE"></span>**PKEY\_WCN\_ConfigState**
</dt> <dd> <dl> <dt>



Indicates if the device has previously been configured by a user. A device is considered to be previously user-configured if a user actively accepts the device settings.

The following table shows the possible configuration states.



| Value | Configuration State     |
|-------|-------------------------|
| 0x1   | Not configured by user. |
| 0x2   | Configured by user.     |



 

**PROPVARIANT** type **VT\_UI1**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_ConnType"></span><span id="pkey_wcn_conntype"></span><span id="PKEY_WCN_CONNTYPE"></span>**PKEY\_WCN\_ConnType**
</dt> <dd> <dl> <dt>



The connection types supported by the enrollee.

The following table shows the possible connection types.



| Value | Connection Type                         | Required/Optional |
|-------|-----------------------------------------|-------------------|
| 0x1   | ESS (infrastructure network connection) | Required          |
| 0x2   | IBSS (ad-hoc network connection)        | Required          |



 

An enrollee must support the required connection types. To determine the value associated with the **PKEY\_WCN\_ConnType** key for an enrollee, combine the values associated with the supported connection types using the bitwise OR operator.

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_DeviceType_Category"></span><span id="pkey_wcn_devicetype_category"></span><span id="PKEY_WCN_DEVICETYPE_CATEGORY"></span>**PKEY\_WCN\_DeviceType\_Category**
</dt> <dd> <dl> <dt>



The major device category of a WCN device.



| Value | Description       |
|-------|-------------------|
| 0x1   | Computer          |
| 0x2   | Input device      |
| 0x3   | Printer           |
| 0x4   | Camera            |
| 0x5   | Storage device    |
| 0x6   | Network           |
| 0x7   | Display           |
| 0x8   | Multimedia Device |
| 0x9   | Gaming Device     |
| 0xa   | Telephone         |



 


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_DeviceType_SubCategory"></span><span id="pkey_wcn_devicetype_subcategory"></span><span id="PKEY_WCN_DEVICETYPE_SUBCATEGORY"></span>**PKEY\_WCN\_DeviceType\_SubCategory**
</dt> <dd> <dl> <dt>



The device subcategory of a WCN device. The subcategory must be interpreted along with the OUI from **PKEY\_WCN\_DeviceType\_SubCategoryOUI**.



| Value | Subcategory                        |
|-------|------------------------------------|
| 0x1   | Personal Computer                  |
| 0x2   | Server                             |
| 0x1   | Printer                            |
| 0x2   | Scanner                            |
| 0x1   | Still-Shot Camera                  |
| 0x1   | Network Storage Device             |
| 0x1   | Access Point                       |
| 0x2   | Router                             |
| 0x3   | Switch                             |
| 0x1   | Television                         |
| 0x2   | Electronic Picture Frame           |
| 0x3   | Digital Projector                  |
| 0x1   | Digital Audio Recorder             |
| 0x2   | Personal Video Recorder            |
| 0x3   | Yamaha Digital Multimedia Receiver |
| 0x1   | Microsoft XBOX                     |
| 0x2   | Microsoft XBOX 360                 |
| 0x3   | Sony Playstation 3                 |
| 0x1   | Windows Mobile                     |



 


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_DeviceType_SubCategoryOUI"></span><span id="pkey_wcn_devicetype_subcategoryoui"></span><span id="PKEY_WCN_DEVICETYPE_SUBCATEGORYOUI"></span>**PKEY\_WCN\_DeviceType\_SubCategoryOUI**
</dt> <dd> <dl> <dt>



The unique manufacturer OUI associated with the device.



| Value                                                                 | Description                                                                      |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **WCN\_VALUE\_DT\_SUBTYPE\_WIFI\_OUI**<br/> 0x50f204<br/> | Indicates the specific manufacturer Organization ID (OUI) for a wireless device. |



 


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_DevicePassword"></span><span id="pkey_wcn_devicepassword"></span><span id="PKEY_WCN_DEVICEPASSWORD"></span>**PKEY\_WCN\_DevicePassword**
</dt> <dd> <dl> <dt>



The origin or 'type' of a password.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x0</td>
<td>The PIN password, obtained from the label, or display will be used.</td>
</tr>
<tr class="even">
<td>0x1</td>
<td>The user has overridden the default password with a manually selected value.
<blockquote>
[!Note]<br />
Not supported in Windows 7.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>0x2</td>
<td>The default PIN password has been overridden by a strong, machine-generated device password value.
<blockquote>
[!Note]<br />
Not supported in Windows 7.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>0x3</td>
<td>The 256-bit rekeying password associated with the device will be used.
<blockquote>
[!Note]<br />
Not supported in Windows 7.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>0x4</td>
<td>A password entered via a push button interface will be used.</td>
</tr>
<tr class="even">
<td>0x5</td>
<td>A PIN has been obtained from the Registrar via a display or other out-of-band method.
<blockquote>
[!Note]<br />
Not supported in Windows 7.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_EncryptType"></span><span id="pkey_wcn_encrypttype"></span><span id="PKEY_WCN_ENCRYPTTYPE"></span>**PKEY\_WCN\_EncryptType**
</dt> <dd> <dl> <dt>



The encryption types supported by the enrollee.

The following table shows the possible encryption types.



| Value  | Encryption Type |
|--------|-----------------|
| 0x0001 | None            |
| 0x0002 | WEP             |
| 0x0004 | TKIP            |
| 0x0008 | AES             |



 

An enrollee must support one or more of the above encryption types. To determine the value associated with the **PKEY\_WCN\_EncryptType** key for an enrollee, combine the values associated with the supported encryption types using the bitwise OR operator.

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_OSVersion"></span><span id="pkey_wcn_osversion"></span><span id="PKEY_WCN_OSVERSION"></span>**PKEY\_WCN\_OSVersion**
</dt> <dd> <dl> <dt>



The operating system version running on the device. The most significant bit is reserved and always set to one. **PROPVARIANT** type **VT\_UI4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_RegistrarType_"></span><span id="pkey_wcn_registrartype_"></span><span id="PKEY_WCN_REGISTRARTYPE_"></span>**PKEY\_WCN\_RegistrarType** 
</dt> <dd> <dl> <dt>



The type of registrar used to transfer the network profile to the enrollee.

The following table shows the possible registrar types.



| Value | Registrar Type                    |
|-------|-----------------------------------|
| 0     | Default registrar                 |
| 1     | OOB Ethernet                      |
| 2     | In-band wireless                  |
| 3     | OOB flash configuration           |
| 4     | OOB Windows Portable Device (WPD) |



 

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_RequestType_"></span><span id="pkey_wcn_requesttype_"></span><span id="PKEY_WCN_REQUESTTYPE_"></span>**PKEY\_WCN\_RequestType** 
</dt> <dd> <dl> <dt>



The mode in which the device operates for setup exchange.

The following table shows the possible modes.



| Value | Request Type Mode                                                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00  | Enrollee; sends Discovery requests only.                                                                                                                      |
| 0x01  | Enrollee; sends Discovery requests and 802.1X data channel setup requests                                                                                     |
| 0x02  | Registrar; responds to requests but does not manage enrollee settings                                                                                         |
| 0x03  | WLAN Manager registrar; responds to requests and manages AP or station (STA) settings using UPnP. This registrar type also derives AP or STA management keys. |



 

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_RfBand"></span><span id="pkey_wcn_rfband"></span><span id="PKEY_WCN_RFBAND"></span>**PKEY\_WCN\_RfBand**
</dt> <dd> <dl> <dt>



The radio frequency band in which an enrollee sends Discovery requests.

The following table shows the possible RF bands.



| Value | RF Band |
|-------|---------|
| 1     | 2.4 GHz |
| 2     | 5.0 GHz |



 

**PROPVARIANT** type **VT\_I4**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_UUID"></span><span id="pkey_wcn_uuid"></span>**PKEY\_WCN\_UUID**
</dt> <dd> <dl> <dt>



Not supported.

**Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:  **

The **UUID** of the device, regardless if the device is enrollee or registrar.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_VendorExtension"></span><span id="pkey_wcn_vendorextension"></span><span id="PKEY_WCN_VENDOREXTENSION"></span>**PKEY\_WCN\_VendorExtension**
</dt> <dd> <dl> <dt>



Vendor extensibility information. This data can be transmitted using the Simple Configuration type-length-value (TLV) framework.

The first 3 octets of the PKEY value contain the vendor identifier. The vendor ID is the SMI Network Management Private Enterprise Code of the vendor. The remaining octets contain the vendor data. For vendor extensions transmitted in 802.11 management frames, the value associated with this PKEY cannot exceed 246 bytes in length.

**PROPVARIANT** type **VT\_VECTOR** \| **VT\_U1**.


</dt> </dl> </dd> <dt>

<span id="PKEY_WCN_Version"></span><span id="pkey_wcn_version"></span><span id="PKEY_WCN_VERSION"></span>**PKEY\_WCN\_Version**
</dt> <dd> <dl> <dt>



The Easy Setup version used by the device. The one byte field is broken into a four bit major part, which contains the most significant bits of the version number, and a four bit minor part, which contains the least significant bits. For example, Easy Setup version 3.2 would be represented as 0x32.

**PROPVARIANT** type **VT\_UI1**.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                 |
| End of client support<br/>    | Windows 8<br/>                                                                                                                                                                 |
| End of server support<br/>    | Windows Server 2012<br/>                                                                                                                                                       |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryKeys.h; </dt> <dt>WcnFunctionDiscoveryKeys.h</dt> </dl> |



## See also

<dl> <dt>

[**Key Definitions**](key-definitions.md)
</dt> </dl>

 

 




