---
Description: 'Represents activation factories that are registered by calling the RoRegisterActivationFactories function.'
ms.assetid: 'D74E5886-45DB-40DE-9740-D14341E78713'
title: 'RO\_REGISTRATION\_COOKIE'
---

# RO\_REGISTRATION\_COOKIE

Represents activation factories that are registered by calling the [**RoRegisterActivationFactories**](roregisteractivationfactories.md) function.


```C++
typedef struct {}* RO_REGISTRATION_COOKIE;
```



## Remarks

The [**RoRegisterActivationFactories**](roregisteractivationfactories.md) function returns a **RO\_REGISTRATION\_COOKIE** when a activatable class factories are registered with the Windows Runtime. The [**RoRevokeActivationFactories**](rorevokeactivationfactories.md) function uses the cookie to remove the class factories.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                     |
| Header<br/>                   | <dl> <dt>Roapi.h</dt> </dl> |



## See also

<dl> <dt>

[**RoRegisterActivationFactories**](roregisteractivationfactories.md)
</dt> <dt>

[**RoRevokeActivationFactories**](rorevokeactivationfactories.md)
</dt> </dl>

 

 




