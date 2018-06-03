---
Description: Defines the PKEYs associated with the WNet Provider.
ms.assetid: d42cbf90-5747-4c46-8a25-a2e43e2ba88e
title: WNet Provider PKEYs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WNet Provider PKEYs

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The following keys are associated with the WNet provider.

<dl> <dt>

<span id="PKEY_WNET_Comment"></span><span id="pkey_wnet_comment"></span><span id="PKEY_WNET_COMMENT"></span>**PKEY\_WNET\_Comment**
</dt> <dd> <dl> <dt>



Corresponds to the **lpComment** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL or WNET\_CONSTRAINTVALUE\_PROPERTIES\_LIMITED. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_DisplayType"></span><span id="pkey_wnet_displaytype"></span><span id="PKEY_WNET_DISPLAYTYPE"></span>**PKEY\_WNET\_DisplayType**
</dt> <dd> <dl> <dt>



Corresponds to the **dwDisplayType** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL or WNET\_CONSTRAINTVALUE\_PROPERTIES\_LIMITED. PROPVARIANT type VT\_UINT.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_LocalName"></span><span id="pkey_wnet_localname"></span><span id="PKEY_WNET_LOCALNAME"></span>**PKEY\_WNET\_LocalName**
</dt> <dd> <dl> <dt>



Corresponds to the **lpLocalName** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_Provider"></span><span id="pkey_wnet_provider"></span><span id="PKEY_WNET_PROVIDER"></span>**PKEY\_WNET\_Provider**
</dt> <dd> <dl> <dt>



Corresponds to the **lpProvider** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_RemoteName"></span><span id="pkey_wnet_remotename"></span><span id="PKEY_WNET_REMOTENAME"></span>**PKEY\_WNET\_RemoteName**
</dt> <dd> <dl> <dt>



Corresponds to the **lpRemoteName** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_Scope"></span><span id="pkey_wnet_scope"></span><span id="PKEY_WNET_SCOPE"></span>**PKEY\_WNET\_Scope**
</dt> <dd> <dl> <dt>



Corresponds to the **dwScope** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL. PROPVARIANT type VT\_UINT.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_Type"></span><span id="pkey_wnet_type"></span><span id="PKEY_WNET_TYPE"></span>**PKEY\_WNET\_Type**
</dt> <dd> <dl> <dt>



Corresponds to the **dwType** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL. PROPVARIANT type VT\_UINT.


</dt> </dl> </dd> <dt>

<span id="PKEY_WNET_Usage"></span><span id="pkey_wnet_usage"></span><span id="PKEY_WNET_USAGE"></span>**PKEY\_WNET\_Usage**
</dt> <dd> <dl> <dt>



Corresponds to the **dwUsage** member of the [**NETRESOURCE**](https://msdn.microsoft.com/library/windows/desktop/aa385353) structure supplied by the NetBIOS provider. This PKEY is present if the PROVIDER\_WNET\_QUERYCONSTRAINT\_PROPERTIES query constraint has a value of WNET\_CONSTRAINTVALUE\_PROPERTIES\_ALL. PROPVARIANT type VT\_UINT.


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

 

 




