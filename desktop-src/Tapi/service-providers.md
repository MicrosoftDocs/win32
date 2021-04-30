---
description: Service providers implement detailed telephony device controls. A telephony service provider (TSP) provides call controls and a media service provider, if it exists, provides control over the media stream.
ms.assetid: eb63d55e-4a2b-4bc0-8001-99772f418d72
title: Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Service Providers

Service providers implement detailed telephony device controls. A telephony service provider (TSP) provides call controls and a media service provider, if it exists, provides control over the media stream.

All telephony service providers execute in the TAPISRV process. Service providers can create threads in the TAPISRV context as needed to do their work, and be confident that none of the resources they create will be destroyed by the exit of any individual application. The TAPI Server translates application commands as needed into a consistent set of commands known as the Telephony Service Provider Interface (TSPI).

Media service providers execute in the process space of the application, allowing for the fast response sometimes required in media controls. The TAPI DLL provides for consistent adherence to the Media Service Provider Interface (MSPI).

For more detailed coverage of the service providers, please see [TAPI Service Provider Overview](./tapi-service-provider-overview.md).

Underneath the telephony service provider DLL, the service provider can use any system functions or other components necessary. These functions include [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) and [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol), which work with independent hardware vendor-designed kernel mode components and services, as well as standard devices such as serial and parallel ports to control external, locally attached devices. They can also access network services (such as RPC, Windows Sockets, and Named Pipes) for client/server telephony.

The Telephony service provider user interface DLL is loaded by TAPI into the process of an application that invokes any of the service provider functions that can display a dialog box (for example, [**TSPI\_lineConfigDialog**](/windows/win32/api/tspi/nf-tspi-tspi_lineconfigdialog)). The service provider can also cause its associated UI DLL to be loaded and executed in the process of an application if the service provider needs to display UI at unexpected times, such as to display the **Talk/Hang-up** dialog box displayed by the Universal Modem Driver (UNIMODEM) when a data modem is used to dial an interactive voice call using [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall) (not normally considered to be a UI-generating function).

The proxy request handler is a full telephony application that normally executes on a telephony server (the same server on which the telephony service provider is executing for the associated line devices). This architecture, rather than the WOSA service provider architecture, is used when a particular service is more appropriately implemented in an application than in a driver on the server. For example, the ACD Agent management functions are implemented in a proxy request handler rather than in a service provider.

The UNIMODEM driver service provider for modem control is available on Windows Server 2003 operating systems, Windows XP, Windows 2000, and Windows NT. Windows Telephony also includes a generic kernel-mode Telephony Service Provider Interface (TSPI) mapper, KMDDSP, that allows service providers to be implemented as kernel-mode device drivers.

 

 
