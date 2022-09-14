---
title: DllSurrogate
description: Enables DLL servers to run in a surrogate process. If an empty string is specified, the system-supplied surrogate is used; otherwise, the value specifies the path of the surrogate to be used.
ms.assetid: ae02d828-9cdb-4faa-8fa9-971da97e27b1
keywords:
- DllSurrogate registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# DllSurrogate

Enables DLL servers to run in a surrogate process. If an empty string is specified, the system-supplied surrogate is used; otherwise, the value specifies the path of the surrogate to be used.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      DllSurrogate = path
```

## Remarks

This is a **REG\_SZ** value that specifies that the class is a DLL that is to be activated in a surrogate process, and the surrogate process to be used. To use the system-supplied generic surrogate process, set *path* to an empty string or **NULL**. To specify another surrogate process, set *path* to the path of the surrogate. As in the specification of the path of a server under the [**LocalServer32**](localserver32.md) key, a full path specification is not necessary. The surrogate must be written to properly communicate with the DCOM service as described in [Writing a Custom Surrogate](writing-a-custom-surrogate.md).

The **DllSurrogate** value must be present for a DLL server to be activated in a surrogate. Activation refers to a call to [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject), [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex), **CoCreateInstanceEx**, [**CoGetInstanceFromFile**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromfile), [**CoGetInstanceFromIStorage**](/windows/desktop/api/Objbase/nf-objbase-cogetinstancefromistorage), or [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject). Running DLLs in a surrogate process provides the benefits of an executable implementation, including fault isolation, the ability to serve multiple clients simultaneously, and allowing the server to provide services to remote clients in a distributed environment.

## Related topics

<dl> <dt>

[**CoRegisterSurrogate**](/windows/desktop/api/combaseapi/nf-combaseapi-coregistersurrogate)
</dt> <dt>

[DLL Surrogates](dll-surrogates.md)
</dt> <dt>

[**DllSurrogateExecutable**](dllsurrogateexecutable.md)
</dt> <dt>

[**ISurrogate**](/windows/win32/api/objidlbase/nn-objidlbase-isurrogate)
</dt> </dl>

 

 