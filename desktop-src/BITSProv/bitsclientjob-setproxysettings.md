---
title: SetProxySettings method of the BitsClientJob class
description: The SetProxySettings method modifies the proxy settings for the BITS transfer job.
ms.assetid: '0fed4286-1a80-4e79-a7c5-e9a542cd05a3'
keywords: ["SetProxySettings method", "SetProxySettings method, BitsClientJob class", "BitsClientJob class, SetProxySettings method"]
topic_type:
- apiref
api_name:
- BitsClientJob.SetProxySettings
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# SetProxySettings method of the BitsClientJob class

The **SetProxySettings** method modifies the proxy settings for the BITS transfer job

## Syntax


```mof
uint32 SetProxySettings(
  [in]           uint16 ProxyUsage,
  [in, optional] string ProxyList,
  [in, optional] string ProxyBypassList
);
```



## Parameters

<dl> <dt>

*ProxyUsage* \[in\]
</dt> <dd>

Specifies whether the user's proxy settings will be used, whether a proxy will be used, or whether application-specific proxy settings will be used. The default is to use the user's proxy settings. This parameter can be set to one of the following values:



| Value                                                                        | Meaning                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Use the Internet Explorer proxy and the proxy bypass list settings that are defined by each user to transfer files. Settings are defined by the user in the local area network (LAN) settings (or dial-up settings, depending on the network connection) in the **Network and Internet** item in **Control Panel**.<br/> |
| <dl> <dt>1</dt> </dl> | Do not use a proxy to transfer files. Use this value when you transfer files within a LAN.<br/>                                                                                                                                                                                                                          |
| <dl> <dt>2</dt> </dl> | Use the application's proxy and the proxy bypass list to transfer files. Use this value if you are not sure that the system settings are correct. Also, use this value when you want to transfer files by using a special account, such as LocalSystem, for which the system settings do not apply.<br/>                 |
| <dl> <dt>3</dt> </dl> | Automatically detect the proxy settings. BITS detects the proxy settings for each file in the BITS transfer job.<br/>                                                                                                                                                                                                    |



 

</dd> <dt>

*ProxyList* \[in, optional\]
</dt> <dd>

Specifies a **null**-terminated string that contains the proxies to use to transfer files. The list is space-delimited. This parameter must be **NULL** if the value of ProxyUsage is set to 0, 1, or 3.

</dd> <dt>

*ProxyBypassList* \[in, optional\]
</dt> <dd>

Specifies a **null**-terminated string that contains an optional list of host names, IP addresses, or both, that can bypass the proxy. The list is space-delimited. This parameter must be **NULL** if the value of ProxyUsage is set to 0, 1, or 3.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 





