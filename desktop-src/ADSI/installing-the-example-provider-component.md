---
title: Installing the Example Provider Component
description: After installing the ADSI SDK, from the installation directory, change directories to the Samples\\NetDs\\ADSI\\Samples\\Provider\\Setup subdirectory. Run Install.bat as described in the README.TXT file.
ms.assetid: 7bf4bf22-38ac-4b0d-946e-5f60c7693707
ms.tgt_platform: multiple
keywords:
- Installing the Example Provider Component ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Installing the Example Provider Component

After installing the ADSI SDK, from the installation directory, change directories to the Samples\\NetDs\\ADSI\\Samples\\Provider\\Setup subdirectory. Run Install.bat as described in the README.TXT file.

The sample ADSI provider will add the following subkeys and values to the registry when Install.bat file is run:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         ADs
            Providers
               Sample = SampleNamespace
```

```
HKEY_CLASSES_ROOT
   SampleNamespace
      Clsid = {F46430D0-CBfB-11CE-A9F7-00AA00B67689}
```

```
HKEY_CLASSES_ROOT
   Sample
      Clsid = {F46430D1-CBfB-11CE-A9F7-00AA00B67689}
```

```
HKEY_CLASSES_ROOT
   CLSID
      {F46430D0-CBfB-11CE-A9F7-00AA00B67689}
         (Default) = Sample Namespace Object
         InprocServer32
            (Default) = adssmp.dll
            ThreadingModel = Both
         ProgID
            (Default) = SampleNamespace
         TypeLib
            (Default) = {F46430D2-CBfB-11CE-A9F7-00AA00B67689}
         Version
            (Default) = 0.0
```

```
HKEY_CLASSES_ROOT
   CLSID
      {F46430D1-CBfB-11CE-A9F7-00AA00B67689}
         (Default) = Sample Provider Object
         InprocServer32
            (Default) = adssmp.dll
            ThreadingModel = Both
         ProgID
            (Default) = Sample
         TypeLib
            (Default) = {F46430D2-CBfB-11CE-A9F7-00AA00B67689}
         Version
            (Default) = 0.0
```

Other registry entries for the example provider component exist because the example provider component implemented its directory hierarchy in the registry. This in no way implies other providers would want to or should do the same.

 

 




