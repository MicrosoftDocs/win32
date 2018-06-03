---
Description: Defines the PKEYs to be used by any Function Discovery provider.
ms.assetid: 356ec8eb-f226-48e3-b0b6-ce35ee3ab6ab
title: General PKEYs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# General PKEYs

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The following are general keys.

<dl> <dt>

<span id="PKEY_Device_InstanceId"></span><span id="pkey_device_instanceid"></span><span id="PKEY_DEVICE_INSTANCEID"></span>**PKEY\_Device\_InstanceId**
</dt> <dd> <dl> <dt>



The instance identifier. The PnP provider uses this key on Windows XP to provide access to the devnode descriptor. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_Device_Interface"></span><span id="pkey_device_interface"></span><span id="PKEY_DEVICE_INTERFACE"></span>**PKEY\_Device\_Interface**
</dt> <dd> <dl> <dt>



The GUID of the interface. The PnP provider uses this key to provide the GUID on interface instances. The key may also be implemented by other providers. PROPVARIANT type VT\_CLSID.


</dt> </dl> </dd> <dt>

<span id="PKEY_Device_Model"></span><span id="pkey_device_model"></span><span id="PKEY_DEVICE_MODEL"></span>**PKEY\_Device\_Model**
</dt> <dd> <dl> <dt>



The model name of the device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_Device_NotPresent"></span><span id="pkey_device_notpresent"></span><span id="PKEY_DEVICE_NOTPRESENT"></span>**PKEY\_Device\_NotPresent**
</dt> <dd> <dl> <dt>



The device presence. This key is used by the PnP provider to show that a device is installed, has not yet been removed, but is not currently online. It may be powered off, unplugged, or the device driver may have marked it not-present. PROPVARIANT type VT\_UINT.


</dt> </dl> </dd> <dt>

<span id="PKEY_FD_Visibility"></span><span id="pkey_fd_visibility"></span><span id="PKEY_FD_VISIBILITY"></span>**PKEY\_FD\_Visibility**
</dt> <dd> <dl> <dt>



The device visibility. This key is used by the PnP provider to show that a device is installed, present, but marked not visible by PnP. PROPVARIANT type VT\_UINT.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_METADATA"></span><span id="pkey_pubsvcs_metadata"></span>**PKEY\_PUBSVCS\_METADATA**
</dt> <dd> <dl> <dt>



The metadata for the published resource. This key is optional. The interpretation of this key is determined by the publisher and the subscriber. The method of interpretation must be determined before the key is used. The key can contain a simple data type (such as an integer), a string containing an XML blob, or a serialized data structure. PROPVARIANT type is VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_METADATA_VERSION"></span><span id="pkey_pubsvcs_metadata_version"></span>**PKEY\_PUBSVCS\_METADATA\_VERSION**
</dt> <dd> <dl> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_NETWORK_PROFILES_ALLOWED"></span><span id="pkey_pubsvcs_network_profiles_allowed"></span>**PKEY\_PUBSVCS\_NETWORK\_PROFILES\_ALLOWED**
</dt> <dd> <dl> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_NETWORK_PROFILES_DEFAULT"></span><span id="pkey_pubsvcs_network_profiles_default"></span>**PKEY\_PUBSVCS\_NETWORK\_PROFILES\_DEFAULT**
</dt> <dd> <dl> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_NETWORK_PROFILES_DENIED"></span><span id="pkey_pubsvcs_network_profiles_denied"></span>**PKEY\_PUBSVCS\_NETWORK\_PROFILES\_DENIED**
</dt> <dd> <dl> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_SCOPE"></span><span id="pkey_pubsvcs_scope"></span>**PKEY\_PUBSVCS\_SCOPE**
</dt> <dd> <dl> <dt>



Not used.


</dt> </dl> </dd> <dt>

<span id="PKEY_PUBSVCS_TYPE"></span><span id="pkey_pubsvcs_type"></span>**PKEY\_PUBSVCS\_TYPE**
</dt> <dd> <dl> <dt>



The resource type for the target service being published. This key is required. The resource type is searchable. The length of the key is limited to 256 bytes. PROPVARIANT type is VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_Write_Time"></span><span id="pkey_write_time"></span><span id="PKEY_WRITE_TIME"></span>**PKEY\_Write\_Time**
</dt> <dd> <dl> <dt>



The time that the property store was last written. This key is used by the registry provider to store the last time the property store was saved to the registry. This key should be considered to be read-only, as any value you set will be ignored and overwritten by the value supplied by the registry provider. PROPVARIANT type is VT\_FILETIME.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryKeys.h</dt> </dl> |



## See also

<dl> <dt>

[**Key Definitions**](key-definitions.md)
</dt> </dl>

 

 




