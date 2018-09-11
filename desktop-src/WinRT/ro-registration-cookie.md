---
Description: Represents activation factories that are registered by calling the RoRegisterActivationFactories function.
ms.assetid: D74E5886-45DB-40DE-9740-D14341E78713
title: RO_REGISTRATION_COOKIE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RO\_REGISTRATION\_COOKIE

Represents activation factories that are registered by calling the [**RoRegisterActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224653(v=VS.85).aspx) function.


```C++
typedef struct {}* RO_REGISTRATION_COOKIE;
```



## Remarks

The [**RoRegisterActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224653(v=VS.85).aspx) function returns a **RO\_REGISTRATION\_COOKIE** when a activatable class factories are registered with the Windows Runtime. The [**RoRevokeActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224655(v=VS.85).aspx) function uses the cookie to remove the class factories.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                     |
| Header<br/>                   | <dl> <dt>Roapi.h</dt> </dl> |



## See also

<dl> <dt>

[**RoRegisterActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224653(v=VS.85).aspx)
</dt> <dt>

[**RoRevokeActivationFactories**](https://msdn.microsoft.com/en-us/library/BR224655(v=VS.85).aspx)
</dt> </dl>

 

 




