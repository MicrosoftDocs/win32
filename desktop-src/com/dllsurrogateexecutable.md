---
title: DllSurrogateExecutable
description: Enables DLL servers to run in a custom surrogate process, in conjunction with the DllSurrogate registry value. If DllSurrogateExecutable is not specified, COM passes NULL as the value for the first parameter of the CreateProcess function.
ms.assetid: faf5dde3-bd67-447b-a88c-e8660dc5228e
keywords:
- DllSurrogateExecutable registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# DllSurrogateExecutable

Enables DLL servers to run in a custom surrogate process, in conjunction with the [**DllSurrogate**](dllsurrogate.md) registry value. If **DllSurrogateExecutable** is not specified, COM passes **NULL** as the value for the first parameter of the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) function.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      DllSurrogateExecutable = file
```

## Remarks

This value is of type **REG\_SZ**. It works in conjunction with the [**DllSurrogate**](dllsurrogate.md) value to prevent any ambiguity when using the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) function. **DllSurrogate** indicates whether a custom surrogate needs to be used, and this information is passed as the first parameter for **CreateProcess**. Depending on the implementation of **CreateProcess**, this information might be ambiguous. If **DllSurrogateExecutable** is specified, COM passes the value as the first parameter of **CreateProcess**. If **DllSurrogateExecutable** is not specified, COM passes **NULL** as the value for the first parameter of **CreateProcess**.

## Related topics

<dl> <dt>

[**CoRegisterSurrogate**](/windows/desktop/api/combaseapi/nf-combaseapi-coregistersurrogate)
</dt> <dt>

[DLL Surrogates](dll-surrogates.md)
</dt> <dt>

[**DllSurrogate**](dllsurrogate.md)
</dt> <dt>

[**ISurrogate**](/windows/win32/api/objidlbase/nn-objidlbase-isurrogate)
</dt> </dl>

 

 