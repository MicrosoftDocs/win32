---
title: DirectML version history
description: DirectML is distributed as a system component of Windows 10, and is available as part of the Windows 10 operating system (OS) in Windows 10, version 1903 (10.0; Build 18362), and newer.
ms.localizationpriority: high
ms.topic: article
ms.date: 11/05/2020
---

# DirectML version history

DirectML is distributed as a system component of Windows 10, and is available as part of the Windows 10 operating system (OS) in Windows 10, version 1903 (10.0; Build 18362), and newer.

Starting with DirectML version 1.4.0, DirectML is also available as a standalone redistributable package (see [Microsoft.AI.DirectML](https://www.nuget.org/packages/Microsoft.AI.DirectML/)), which is useful for applications that wish to use a fixed version of DirectML, or when running on older versions of Windows 10.

DirectML follows the [semantic versioning](https://semver.org/) conventions. That is, version numbers follow the form `major.minor.patch`. The first release of DirectML has a version of 1.0.0.

## Version table

|DirectML version|Feature level supported (see [DirectML feature level history](./dml-feature-level-history.md))|DML_TARGET_VERSION|First available in|First available in (Redistributable)|
|-|-|-|-|-|-|
|1.5.0|DML_FEATURE_LEVEL_3_1|`0x3100`|N/A|[DirectML-1.5.0](https://www.nuget.org/packages/Microsoft.AI.DirectML/1.5.0)|
|1.4.0<sup>1</sup>|DML_FEATURE_LEVEL_3_0|`0x3000`|N/A|[DirectML-1.4.0](https://www.nuget.org/packages/Microsoft.AI.DirectML/1.4.0)|
|1.1.0|DML_FEATURE_LEVEL_2_0|`0x2000`|Windows 10, version 2004 (10.0; Build 19041) (Windows 10 May 2020 Update). Aka "20H1".|N/A|
|1.0.0|DML_FEATURE_LEVEL_1_0|`0x1000`|Windows 10, version 1903 (10.0; Build 18362) (Windows 10 May 2019 Update). Aka "19H1".|N/A|

<sup>1</sup> The 1.2.0 and 1.3.0 intermediate releases of DirectML weren't made widely available.

## Selecting a DirectML target version

For convenience, certain features in the `DirectML.h` header file are declared conditionally based on the value of the `DML_TARGET_VERSION` macro. By setting the `DML_TARGET_VERSION` macro to certain values, you can exclude parts of `DirectML.h` from your application.

That can be helpful if you're using a newer copy of `DirectML.h`, but you're targeting a lower version of the DirectML binary, because it ensures that any attempt to use features beyond the chosen target level won't compile. This mechanism is similar to the `NTDDI_VERSION` macro (see [Macros for conditional declarations](../winprog/using-the-windows-headers.md#macros-for-conditional-declarations)).

Here are the valid values for the `DML_TARGET_VERSION` macro.

|DML_TARGET_VERSION|Effect|
|-|-|
|`0x3000`|Any features that require a version of DirectML newer than **1.4.0** are excluded from `DirectML.h`.|
|`0x2000`|Any features that require a version of DirectML newer than **1.1.0** are excluded from `DirectML.h`.|
|`0x1000`|Any features that require a version of DirectML newer than **1.0.0** are excluded from `DirectML.h`.|
|*Not set*|The target version is selected automatically for you. See below for details.|

If `DML_TARGET_VERSION` is not set, then it is selected automatically by the following.

* If the `DML_TARGET_VERSION_USE_LATEST` macro is defined, then the latest target version is selected.
* Otherwise, the target version is selected based on the value of the `NTDDI_VERSION` macro.
  *  `NTDDI_WIN10_19H1` results in a target version of `0x1000`.
  *  `NTDDI_WIN10_VB` results in a target version of `0x2000`.
  *  If `NTDDI_VERSION` is not defined, then the latest target version is selected (as if `DML_TARGET_VERSION_USE_LATEST` were specified).

### Example

Consider an application using version 10.0.19041.0 (Windows 10, version 2004) of the Windows Software Development Kit (SDK). From the table above, the version of DirectML that this corresponds to is 1.1.0, and the corresponding `DML_TARGET_VERSION` is `0x2000`.

If you don't set either the `DML_TARGET_VERSION` nor the `NTDDI_VERSION` macros, then the selected target version will default to `0x2000`, and everything in `DirectML.h` will be available for use.

If you want your application to be able to run on Windows 10, version 1903 (10.0; Build 18362), then you could `#define DML_TARGET_VERSION 0x1000`, which will exclude all content in `DirectML.h` that isn't supported by DirectML version 1.0.0. This ensures that any attempt to use functionality that requires a greater version will fail to compile.

## DirectML version versus feature level

The DirectML version (for example, 1.0.0, or 1.4.0) describes a particular release of DirectML, including its associated `DirectML.h` header file and `.lib` file.

The feature level (for example, `DML_FEATURE_LEVEL_1_0`, or `DML_FEATURE_LEVEL_2_0`) describes the capability of the underlying implementation of the API, which can vary from the version of `DirectML.h` used.

For example, an application building against a newer SDK, but running on an older version of Windows, might (at runtime) see a lower supported feature level, even if it's compiled against the latest SDK.

## See also

* [DirectML feature level history](./dml-feature-level-history.md)
* [DML_FEATURE_LEVEL enumeration](/windows/win32/api/directml/ne-directml-dml_feature_level)
* [Microsoft.AI.DirectML redistributable package](https://www.nuget.org/packages/Microsoft.AI.DirectML/)