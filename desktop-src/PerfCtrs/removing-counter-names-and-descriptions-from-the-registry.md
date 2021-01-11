---
description: The unlodctr tool removes the registry entries created by lodctr.
ms.assetid: 83c0fb91-857c-40d9-8fb8-8734c1b573c4
title: Removing Counter Names and Descriptions from the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Removing Counter Names and Descriptions from the Registry

The **unlodctr** tool removes the registry entries created by **lodctr**. The application name that you pass to **unlodctr** must match the [name of the application key](creating-the-applications-performance-key.md) that you created under the **Services** key. For details on running **unlodctr** see, Help and Support Center.

## Using unlodctr

The **unlodctr** tool looks up the first and last counter and help index values using the like named registry values under your application's **Performance** key. The **unlodctr** tool uses the range of index values to remove the text from **Counters** and **Help** values for each language identifier.

Using the index values, **unlodctr** makes the following changes to the registry.

```
HKEY_LOCAL_MACHINE
   \SOFTWARE
      \Microsoft
         \Windows NT
            \CurrentVersion
               \Perflib
                  Last Counter = updated if changed
                  Last Help = updated if changed
                  \009
                     Counters = application text removed
                     Help = application text removed
                  \supported language, other than English
                     Counters = application text removed
                     Help = application text removed
```

The **unlodctr** tool also removes the **First Counter**, **Last Counter**, **First Help**, **Last Help**, and **Object List** values from the application's **Performance** key located at **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\*application-name*\\**Performance**.

> [!Note]  
> The unloading function of **unlodctr**, [**UnloadPerfCounterTextStrings**](/windows/desktop/api/Loadperf/nf-loadperf-unloadperfcountertextstringsa), is declared in Loadperf.h and exported from Loadperf.dll. This allows you to call this function directly from your uninstall program.

 

 

 



