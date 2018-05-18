---
title: MDM\_RemoteAppUserCookie class
description: Retrieves information that a device needs to subscribe to a remote application server.
ms.assetid: '4b185a3a-6f4d-467a-8f75-19d874d9b338'
keywords: ["MDM_RemoteAppUserCookie class MDM App Management", "MDM_RemoteAppUserCookie class MDM App Management , described"]
topic_type:
- apiref
api_name:
- MDM_RemoteAppUserCookie
- MDM_RemoteAppUserCookie.FeedUrl
- MDM_RemoteAppUserCookie.Cookie
- MDM_RemoteAppUserCookie.CookieHash
api_location:
- MDMAppProv.dll
api_type:
- DllExport
---

# MDM\_RemoteAppUserCookie class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Retrieves information that a device needs to subscribe to a remote application server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_RemoteAppUserCookie
{
  string FeedUrl;
  string Cookie;
  string CookieHash;
};
```

## Members

The **MDM\_RemoteAppUserCookie** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_RemoteAppUserCookie** class has these properties.

<dl> <dt>

**Cookie**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets an authentication cookie that allows the device to subscribe to the remote application server.

</dd> <dt>

**CookieHash**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a server generated hash of the authentication cookie for the remote application server.

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

 

 





