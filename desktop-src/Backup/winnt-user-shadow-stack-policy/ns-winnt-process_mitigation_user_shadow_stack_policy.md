---
UID: NS:winnt._PROCESS_MITIGATION_USER_SHADOW_STACK_POLICY
title: PROCESS_MITIGATION_USER_SHADOW_STACK_POLICY
targetos: Windows
description: Contains process mitigation policy settings for Hardware-enforced Stack Protection (HSP).
req.construct-type: structure
req.header: winnt.h
dev_langs:
 - c++
---

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Contains process mitigation policy settings for Hardware-enforced Stack Protection (HSP). The [GetProcessMitigationPolicy](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy) and [SetProcessMitigationPolicy](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy) functions use this structure.

## Syntax
```cpp
typedef struct _PROCESS_MITIGATION_USER_SHADOW_STACK_POLICY {
  union {
    DWORD Flags;
    struct {
      DWORD EnableUserShadowStack : 1;
      DWORD ReservedFlags : 31;
    } DUMMYSTRUCTNAME;
  } DUMMYUNIONNAME;
} PROCESS_MITIGATION_USER_SHADOW_STACK_POLICY, *PPROCESS_MITIGATION_USER_SHADOW_STACK_POLICY;
```

## Members

`DUMMYUNIONNAME`

`DUMMYUNIONNAME.Flags`

This member is reserved for system use.

`DUMMYUNIONNAME.DUMMYSTRUCTNAME`

`DUMMYUNIONNAME.DUMMYSTRUCTNAME.EnableUserShadowStack`

If TRUE, Hardware-enforced Stack Protection is enabled for the process in compatibility mode.
This means that the CPU verifies function return addresses at runtime by employing a shadow stack mechanism, if supported by the hardware.
In compatibility mode, only shadow stack violations occurring in modules compiled with [CETCOMPAT](/cpp/build/reference/cetcompat) are fatal.
This field cannot be changed via [SetProcessMitigationPolicy](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy).


`DUMMYUNIONNAME.DUMMYSTRUCTNAME.ReservedFlags`

This member is reserved for system use.


## See Also

[CETCOMPAT](/cpp/build/reference/cetcompat)

[GetProcessMitigationPolicy](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy)

[SetProcessMitigationPolicy](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy)

[winnt.h header](/windows/win32/api/winnt/)
