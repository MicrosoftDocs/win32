---
Description: Represents activation factories that are registered by calling the RoRegisterActivationFactories function.
ms.assetid: D74E5886-45DB-40DE-9740-D14341E78713
title: RO\_REGISTRATION\_COOKIE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RO\_REGISTRATION\_COOKIE

Represents activation factories that are registered by calling the [**RoRegisterActivationFactories**](/windows/win32/roapi/nf-roapi-roregisteractivationfactories?branch=master) function.


```C++
typedef struct {}* RO_REGISTRATION_COOKIE;
```



## Remarks

The [**RoRegisterActivationFactories**](/windows/win32/roapi/nf-roapi-roregisteractivationfactories?branch=master) function returns a **RO\_REGISTRATION\_COOKIE** when a activatable class factories are registered with the Windows Runtime. The [**RoRevokeActivationFactories**](/windows/win32/roapi/nf-roapi-rorevokeactivationfactories?branch=master) function uses the cookie to remove the class factories.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                     |
| Header<br/>                   | <dl> <dt>Roapi.h</dt> </dl> |



## See also

<dl> <dt>

[**RoRegisterActivationFactories**](/windows/win32/roapi/nf-roapi-roregisteractivationfactories?branch=master)
</dt> <dt>

[**RoRevokeActivationFactories**](/windows/win32/roapi/nf-roapi-rorevokeactivationfactories?branch=master)
</dt> </dl>

 

 




