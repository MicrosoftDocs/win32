---
title: MDM\_RemoteApplication class
description: Retrieves information about a remote application on a device that is managed by the Mobile Device Management (MDM) service.
ms.assetid: '36f5903e-b194-42c7-8732-f3bf631fb818'
keywords: ["MDM_RemoteApplication class MDM App Management", "MDM_RemoteApplication class MDM App Management , described"]
topic_type:
- apiref
api_name:
- MDM_RemoteApplication
- MDM_RemoteApplication.FeedUrl
- MDM_RemoteApplication.AppId
api_location:
- MDMAppProv.dll
api_type:
- DllExport
---

# MDM\_RemoteApplication class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Retrieves information about a remote application on a device that is managed by the Mobile Device Management (MDM) service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_RemoteApplication
{
  string FeedUrl;
  string AppId;
};
```

## Members

The **MDM\_RemoteApplication** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_RemoteApplication** class has these properties.

<dl> <dt>

**AppId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets a key that specifies the name of the remote application.

</dd> <dt>

**FeedUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets a key that specifies the URL of the remote application server.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| Namespace<br/>                | Root\\cimv2\\mdm<br/>                                                               |
| MOF<br/>                      | <dl> <dt>MDMAppProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMAppProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Application Provider Classes](https://msdn.microsoft.com/library/dn610374)
</dt> </dl>

 

 





