---
Description: The following are standard MSPI methods that all MSPs must implement. Primary documentation for these methods exists in the Media Service Provider Interface (MSPI) Reference section.
ms.assetid: 22d4828e-f439-44ca-aa6c-f7f18c5fd64f
title: CMSPAddress MSPI Methods Implemented
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CMSPAddress MSPI Methods Implemented

The following are standard MSPI methods that all MSPs must implement. Primary documentation for these methods exists in the [Media Service Provider Interface (MSPI) Reference](media-service-provider-interface-mspi-reference.md) section.



| CMSPAddress methods                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Initialize**](/windows/desktop/api/msp/nf-msp-itmspaddress-initialize)                                                | (Interface [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress)) Called by TAPI3 when this MSP is first created.                                                                                                                                                                                                                                                                                                   |
| [**ShutDown**](/windows/desktop/api/msp/nf-msp-itmspaddress-shutdown)                                                    | (Interface [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress)) Called by TAPI3 when this address is not in use any more.                                                                                                                                                                                                                                                                                         |
| [**ReceiveTSPData**](/windows/desktop/api/msp/nf-msp-itmspaddress-receivetspdata)                                        | (Interface [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress)) Called by TAPI3 when the TSP sends data to this MSP address object.                                                                                                                                                                                                                                                                               |
| [**GetEvent**](/windows/desktop/api/msp/nf-msp-itmspaddress-getevent)                                                    | (Interface [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress)) Called by TAPI3 to get detailed information about an event.                                                                                                                                                                                                                                                                                       |
| [**get\_StaticTerminals**](https://msdn.microsoft.com/en-us/library/ms733180(v=VS.85).aspx)                        | (Interface [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)) OLE Automation wrapper for the helper function [**GetStaticTerminals**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getstaticterminals).                                                                                                                                                                                                                            |
| [**EnumerateStaticTerminals**](https://msdn.microsoft.com/en-us/library/ms733174(v=VS.85).aspx)               | (Interface [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)) Enumeration wrapper for the helper function [**GetStaticTerminals**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getstaticterminals).                                                                                                                                                                                                                               |
| [**get\_DynamicTerminalClasses**](https://msdn.microsoft.com/en-us/library/ms733178(v=VS.85).aspx)          | (Interface [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)) OLE Automation wrapper for the helper function [**GetDynamicTerminalClasses**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getdynamicterminalclasses).                                                                                                                                                                                                              |
| [**EnumerateDynamicTerminalClasses**](https://msdn.microsoft.com/en-us/library/ms733173(v=VS.85).aspx) | (Interface [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)) Enumeration wrapper for the helper function [**GetDynamicTerminalClasses**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getdynamicterminalclasses).                                                                                                                                                                                                                 |
| [**CreateTerminal**](https://msdn.microsoft.com/en-us/library/ms733172(v=VS.85).aspx)                                   | (Interface [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)) This method is called by the application to create a dynamic terminal. It schedules a work item on the MSP's worker thread, which, when executed, asks the Terminal Manager to create a dynamic terminal. The derived class can override this method to have its own way of creating a dynamic terminal.                                |
| [**GetDefaultStaticTerminal**](https://msdn.microsoft.com/en-us/library/ms733176(v=VS.85).aspx)               | (Interface [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)) This method is called by the application to get the default static terminal for a specified type and direction. It updates the default terminal list (if needed) and returns the interface pointer. The derived class can override this method to have its own way of deciding which terminal is the default. Locks the terminal lists. |



 

 

 



