---
Description: When using the RegisterDlls INF directive to self-register DLLs, callers of SetupInstallFromInfSection may receive notifications on each file as it is registered or unregistered.
ms.assetid: 0faf277c-7805-478f-9cec-0dd7b6acdb0e
title: SPFILENOTIFY\_STARTREGISTRATION message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_STARTREGISTRATION message

When using the **RegisterDlls** INF directive to self-register DLLs, callers of [**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master) may receive notifications on each file as it is registered or unregistered. To send a **SPFILENOTIFY\_STARTREGISTRATION** notification to the callback routine once before registering a file, include SPINST\_REGISTERCALLBACKAWARE plus SPINST\_REGSVR in the *Flags* parameter of **SetupInstallFromInfSection**. To send notification of unregistration, include SPINST\_REGISTERCALLBACKAWARE plus SPINST\_UNREGSVR in the *Flags* parameter.

The callback routine specified by the *MsgHandler* parameter of [**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master) must be the type [PSP\_FILE\_CALLBACK](/windows/win32/setupapi/?branch=master). Set the *Context* parameter to the same *Context* specified in **SetupInstallFromInfSection**. Set the *Notification* parameter to **SPFILENOTIFY\_STARTREGISTRATION**.


```C++
SPFILENOTIFY_STARTREGISTRATION
  Param1 = (UINT_PTR) pointer to file information;
  Param2 = (UINT_PTR) file registration or unregistration;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**SP\_REGISTER\_CONTROL\_STATUS**](/windows/win32/Setupapi/ns-setupapi-_sp_register_control_statusa?branch=master) structure containing information about the file being registered or unregistered. The member **cbsize** should be set to the size of the structure. The **FileName** member should be set to the fully qualified path of the file being registered. **Win32Error** is not used and should be set to NO\_ERROR. **FailureCode** is not used and should be set to SPREG\_SUCCESS.

</dd> <dt>

*Param2* 
</dt> <dd>

If the file is being registered, *Param2* should be set to a pointer to a nonzero value. If the file is being unregistered, *Param2* should be set to a pointer to zero.

</dd> </dl>

## Return value

After receiving notification, the callback function may return one of the following values.



| Return code                                                                                  | Description                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl> | Do not register or unregister the file and stop processing the INF section.<br/>             |
| <dl> <dt>**FILEOP\_DOIT**</dt> </dl>  | Register or unregister the file and continue processing the INF section.<br/>                |
| <dl> <dt>**FILE\_SKIP**</dt> </dl>    | Skip registration or unregistration of the file but continue processing the INF section<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**SetupInstallFromInfSection**](/windows/win32/Setupapi/nf-setupapi-setupinstallfrominfsectiona?branch=master)
</dt> <dt>

[**SPFILENOTIFY\_ENDREGISTRATION**](spfilenotify-endregistration.md)
</dt> </dl>

 

 




