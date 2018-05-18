---
title: IPC\_AAD\_APPLICATION\_ID structure
description: Provides identifying information for the Azure Active Directory application using the Rights Management Services client.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'F2AE2517-F7CB-42DC-BE1B-039BB990E7DA'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_AAD_APPLICATION_ID structure Active Directory Rights Management Services SDK 2.0", "PIPC_AAD_APPLICATION_ID structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_AAD_APPLICATION_ID
api_location:
- Ipcbase.h
api_type:
- HeaderDef
---

# IPC\_AAD\_APPLICATION\_ID structure

Provides identifying information for the Azure Active Directory application using the Rights Management Services client.

## Syntax


```C++
typedef struct _IPC_AAD_APPLICATION_ID {
  DWORD    cbSize;
  LPCWSTR  wszClientId;
  LPCWSTR  wszRedirectUri;
} IPC_AAD_APPLICATION_ID, *PIPC_AAD_APPLICATION_ID;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size of the structure and needs to be initialized to `sizeof(IPC_AAD_APPLICATION_ID)`.

</dd> <dt>

**wszClientId**
</dt> <dd>

String representation of the GUID client identified assigner of your Azure Active Directory application.

</dd> <dt>

**wszRedirectUri**
</dt> <dd>

Redirection URI you provided to Azure Active Directory when creating your application.

</dd> </dl>

## Remarks

For a detailed example, see [ADAL authentication for your RMS enabled application](authentication-with-adal.md).

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



 

 





