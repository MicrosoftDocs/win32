---
title: IMsgrSessionManager RegisterApplication method
description: Registers an application for use with a Messenger client.
ms.assetid: 8ae7f060-52ca-410b-8ba0-35f689a5af3d
keywords:
- RegisterApplication method Windows Messenger
- RegisterApplication method Windows Messenger , IMsgrSessionManager interface
- IMsgrSessionManager interface Windows Messenger , RegisterApplication method
topic_type:
- apiref
api_name:
- IMsgrSessionManager.RegisterApplication
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMsgrSessionManager::RegisterApplication method

\[**RegisterApplication** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Registers an application for use with a Messenger client.

## Syntax


```C++
HRESULT RegisterApplication(
  [in] BSTR bstrAppGUID,
  [in] BSTR bstrAppName,
  [in] BSTR bstrAppURL,
  [in] BSTR bstrPath,
  [in] LONG ulFlags
);
```



## Parameters

<dl> <dt>

*bstrAppGUID* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the GUID of the application. Maximum character length is 39.

</dd> <dt>

*bstrAppName* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the application name. Maximum character length is 256.

</dd> <dt>

*bstrAppURL* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the URL from which the application can be downloaded. Maximum character length is 256.

</dd> <dt>

*bstrPath* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the absolute path to the application's executable. Maximum character length is 260.

</dd> <dt>

*ulFlags* \[in\]
</dt> <dd>

Type: **LONG**

**LONG** that specifies the flag. This value should always be 0, otherwise this function returns E\_INVALIDARG.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | The application was registered successfully.<br/>                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | One of the parameters passed to the method was not valid.<br/>                                                        |
| <dl> <dt>**SR\_APP\_ALREADY\_REGISTERED**</dt> </dl> | The application you are registering has already been registered. (See the following Remarks section).<br/>            |
| <dl> <dt>**REGDB\_E\_WRITEREGDB**</dt> </dl>         | The method failed to write the information to the registry.<br/>                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | The absolute path to the application cannot be resolved or an application with this GUID is already registered. <br/> |



 

## Remarks

Attempting to register an application with a GUID already registered for use with a Messenger client returns **SR\_APP\_ALREADY\_REGISTERED**.

After registering an application, if you want to re-register it to update any of its parameters (*bstrAppName*, *bstrAppURL*, *bstrPath*, or *ulFlags*) except for *bstrAppGUID*, you need to unregister the application first. For example, if you have an application already registered with *bstrAppName* set to someFile.exe and the next version of someFile.exe takes command line arguments such as someFile.exe /s, which you want to use with a Messenger client, you must unregister the application before re-registering it, assuming the *bstrAppGUID* did not change. However, if you specify a different *bstrAppGUID* that is unique and not in use by any other application, you are not required to unregister the application first.

The following table lists the error codes returned by this method.



| Error Code | Meaning                                                                  |
|------------|--------------------------------------------------------------------------|
| 0x80004005 | The session information cannot be retrieved due to a catastrophic error. |
| 0x80070057 | One of the parameters passed to the method was not valid.                |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IMsgrSessionManager**](im-imsgrsessionmanager.md)
</dt> <dt>

[**UnRegisterApplication**](im-imsgrsessionmanager-unregisterapplication-method.md)
</dt> <dt>

[**SESSION\_RESULT**](im-session-result-enum.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





