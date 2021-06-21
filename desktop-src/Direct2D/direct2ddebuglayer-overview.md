---
title: Direct2D Debug Layer Overview
description: Direct2D Debug Layer Overview
ms.assetid: 7c28e00b-ebb9-4b79-939c-64eade1351ad
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D Debug Layer Overview

The Direct2D debug layer provides design-time debug messages for you to minimize runtime application failure. This overview describes the basics of the Direct2D debug layer. It assumes that you are familiar with creating basic Direct2D applications.

This overview contains the following sections.

-   [What Is the Direct2D Debug Layer](#what-is-the-direct2d-debug-layer)
-   [Installing the Direct2D Debug Layer](#installing-the-direct2d-debug-layer)
-   [Enabling the Debug Layer](#enabling-the-debug-layer)
-   [Debug Levels](#debug-levels)
-   [Related topics](#related-topics)

## What Is the Direct2D Debug Layer

The Direct2D debug layer, implemented separately from Direct2D in its own DLL named d2d1debug.dll, provides debug messages to enable you to accurately use Direct2D functions. The debug messages often result from API contract violations such as invalid parameters (could be Direct3D-related), invalid resources, threading violations, and performance issues such as using a layer when a clip would suffice. To specify how much information is traced by the debug layer, you can specify one of the three debug levels: information, warning, and error; and a message of level error triggers the breakpoint to help you debug.

## Installing the Direct2D Debug Layer

For instructions on installing the debug layer, see [Installing the Direct2D Debug Layer](installing-the-direct2d-debug-layer.md).

## Enabling the Debug Layer

To enable the debug layer in your application, specify a [**D2D1\_DEBUG\_LEVEL**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_debug_level) value other than **D2D1\_DEBUG\_LEVEL\_NONE** when you create a factory with the [**D2D1CreateFactory**](/windows/desktop/api/d2d1/nf-d2d1-d2d1createfactory) function.

> [!Note]  
> If the Direct2D debug layer is enabled, the Direct2D color management effect (CLSID\_D2D1ColorManagement) may cause an access violation when setting a color context. The workaround is to disable the debug layer when using the color management effect

 

Enabling the debug layer for a factory also enables debugging information for any object created by that factory.

The following example enables the debug layer for a factory when the application is compiled for the DEBUG build configuration.


```C++
        // If you set the options.debugLevel to D2D1_DEBUG_LEVEL_NONE,
        // the debug layer is not enabled.
#if defined(DEBUG) || defined(_DEBUG)
        D2D1_FACTORY_OPTIONS options;
        options.debugLevel = D2D1_DEBUG_LEVEL_INFORMATION;

        hr = D2D1CreateFactory(
            D2D1_FACTORY_TYPE_SINGLE_THREADED,
            options,
            &m_pD2DFactory
            );
#else
        hr = D2D1CreateFactory(
            D2D1_FACTORY_TYPE_SINGLE_THREADED,
            &m_pD2DFactory
            );
#endif
```



> [!Note]  
> If no factory options are specified or a debug level of "none" is specified, the debug layer is not invoked. The debug layer should never be active in the release version of an application.

 

The next section describes the different debug levels defined by the [**D2D1\_DEBUG\_LEVEL**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_debug_level) enumeration.

## Debug Levels

The [**D2D1\_DEBUG\_LEVEL**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_debug_level) enumeration specifies three debug levels: D2D1\_DEBUG\_LEVEL\_ERROR (error), D2D1\_DEBUG\_LEVEL\_WARNING (warning), and D2D1\_DEBUG\_LEVEL\_INFORMATION (information). These levels are interpreted as follows:

-   **Error:** Direct2D sends severe error messages to the debug layer. For example, breaking a threading constraint will generate a severe error.

-   **Warning:** Direct2D sends error messages and warnings to the debug layer so that you can address any of these messages.

-   **Information:** Direct2D sends error messages, warnings, and additional diagnostic information to the debug layer. For example, performance improvement messages will be sent at this debug level.

The value D2D1\_DEBUG\_LEVEL\_NONE (none) indicates that Direct2D does not provide any debugging output.

## Related topics

<dl> <dt>

[Debug Messages](direct2ddebuglayer-debugmessages.md)
</dt> </dl>

 

 




