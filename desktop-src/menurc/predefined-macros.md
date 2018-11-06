---
title: Predefined Macros
description: RC does not support the ANSI C predefined macros (\_\_DATE\_\_, \_\_FILE\_\_, \_\_LINE\_\_, \_\_STDC\_\_, \_\_TIME\_\_, \_\_TIMESTAMP\_\_). Therefore, you cannot include these macros in header files that you will include in your resource script.
ms.assetid: 2098d4a4-7c6f-4cdc-9c02-3d55907f8888
ms.topic: article
ms.date: 05/31/2018
---

# Predefined Macros

RC does not support the ANSI C predefined macros (**\_\_DATE\_\_**, **\_\_FILE\_\_**, **\_\_LINE\_\_**, **\_\_STDC\_\_**, **\_\_TIME\_\_**, **\_\_TIMESTAMP\_\_**). Therefore, you cannot include these macros in header files that you will include in your resource script.

RC does define RC\_INVOKED, which enables you conditionally compile portions of your header files, depending on whether the compiler is your C compiler or the RC compiler. This is important because the RC compiler supports only a subset of the statements a C compiler would support.

To conditionally compile your code with the RC compiler, surround code that RC cannot compile with \#ifndef RC\_INVOKED and **\#endif**.

The following example is taken from the SDK samples. It demonstrates how to create a header file that can be compiled conditionally.

``` syntax
#ifndef RC_INVOKED
#pragma message("Including CntrOutl.H from " __FILE__)
#endif
```

 

 




