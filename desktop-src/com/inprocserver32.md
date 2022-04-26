---
title: InprocServer32
description: Registers a 32-bit in-process server and specifies the threading model of the apartment the server can run in.
ms.assetid: 4edbbd9d-7ea1-4476-aee7-eaf30e54db8d
keywords:
- InprocServer32 registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# InprocServer32

Registers a 32-bit in-process server and specifies the threading model of the apartment the server can run in.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      InprocServer32
         (Default) = path
         ThreadingModel = value
```

## Remarks

**ThreadingModel** is a **REG\_SZ** value the specifies the threading model. The possible values are shown in the following table.



| Value     | Description                                |
|-----------|--------------------------------------------|
| Apartment | Single-threaded apartment                  |
| Both      | Single-threaded or multithreaded apartment |
| Free      | Multithreaded apartment                    |
| Neutral   | Neutral apartment                          |



 

You must use the same value for every object provided by the in-process server.

If **ThreadingModel** is not present or is not set to a value, the server is loaded into the first apartment that was initialized in the process. This apartment is sometimes referred to as the main single-threaded apartment (STA). If the first STA in a process is initialized by COM, rather than by an explicit call to [**CoInitialize**](/windows/desktop/api/Objbase/nf-objbase-coinitialize) or [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex), it is called the host STA. For example, COM creates a host STA if an in-process server to be loaded requires an STA but there is currently no STA in the process.

Whenever possible, the in-process server is loaded in the same apartment as the client that loads it. If the threading model of the client apartment is not compatible with the model specified, the server is loaded as indicated in the following table.



| Threading model of server | Apartment server is run in |
|---------------------------|----------------------------|
| <\not specified\>     | Main STA                   |
| Both                      | Same apartment as client   |
| Free                      | Multithreaded apartment    |
| Neutral                   | Neutral apartment          |



 

If the threading model of the server is Apartment, the apartment the server is loaded in depends on the apartment the client is running in, as indicated in the following table.



| Apartment client is run in | Apartment server is run in |
|----------------------------|----------------------------|
| Multithreaded              | Host STA                   |
| Neutral (on STA thread)    | Same apartment as client   |
| Neutral (on MTA thread)    | Host STA                   |



 

COM can also create a host multithreaded apartment (MTA). If a client in a single-threaded apartment requests an in-process server whose threading model is Free when there is no MTA in the process, COM creates a host MTA and loads the server into it.

For a 32-bit in-process server, the [**InprocHandler32**](inprochandler32.md), [**InprocServer**](inprocserver.md), **InprocServer32**, and [**Insertable**](insertable.md) keys must be registered. The **InprocServer** entry is needed only for backward compatibility. If it is missing, the class still works but it cannot be loaded in 16-bit applications.

If a container is searching the registry for an in-process server, the 16-bit version has priority with a 16-bit container and the 32-bit version has priority with a 32-bit container.

## Related topics

<dl> <dt>

[**InprocServer**](inprocserver.md)
</dt> </dl>

 

 




