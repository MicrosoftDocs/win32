---
title: Registry Values Example
description: The following example shows possible data for some of the authentication protocol registry values.
ms.assetid: 07772af0-db56-4cc6-ad72-cf79d3813883
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# Registry Values Example

The following example shows possible data for some of the authentication protocol registry values.

```text
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            Rasman
               PPP
                  EAP
                     40
                        Path
                        FriendlyName
                        ConfigUIPath
                        IdentityPath
                        InteractiveUIPath
                        RequireConfigUI
                        ConfigCLSID
                        StandaloneSupported
```

| Key Name            | Datatype        | Value                                  |
|---------------------|-----------------|----------------------------------------|
| Path                | REG\_EXPAND\_SZ | %SystemRoot%\\system32\\sample.dll     |
| FriendlyName        | REG\_SZ         | Sample EAP Protocol                    |
| ConfigUIPath        | REG\_EXPAND\_SZ | %SystemRoot%\\system32\\sample.dll     |
| IdentityPath        | REG\_EXPAND\_SZ | %SystemRoot%\\system32\\sample.dll     |
| InteractiveUIPath   | REG\_EXPAND\_SZ | %SystemRoot%\\system32\\sample.dll     |
| RequireConfigUI     | REG\_DWORD      | 1                                      |
| ConfigCLSID         | REG\_SZ         | {0000031A-0000-0000-C000-000000000046} |
| StandaloneSupported | REG\_DWORD      | 1                                      |
