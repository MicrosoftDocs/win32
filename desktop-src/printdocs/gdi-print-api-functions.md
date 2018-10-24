---
Description: GDI Print API Functions
ms.assetid: cf3f4a61-8858-4c91-a778-d2a65998ef70
title: GDI Print API Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GDI Print API Functions

## In this section



| Function                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortDoc**](/windows/desktop/api/Wingdi/nf-wingdi-abortdoc)<br/>                                     | The [**AbortDoc**](https://msdn.microsoft.com/library/windows/desktop/dd162456) function stops the current print job and erases everything drawn since the last call to the [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca) function.<br/>                                                                                                                                                                                                 |
| [*AbortProc*](/windows/desktop/api/Wingdi/nc-wingdi-abortproc)<br/>                                     | The [**AbortProc**](https://msdn.microsoft.com/library/windows/desktop/dd162459) function is an application-defined callback function used with the [**SetAbortProc**](/windows/desktop/api/Wingdi/nf-wingdi-setabortproc) function. It is called when a print job is to be canceled during spooling. The **ABORTPROC** type defines a pointer to this callback function. **AbortProc** is a placeholder for the application-defined function name.<br/> |
| [**DeviceCapabilities**](/windows/desktop/api/WinGdi/nf-wingdi-devicecapabilitiesa)<br/>                 | The [**DeviceCapabilities**](https://msdn.microsoft.com/library/windows/desktop/dd183552) function retrieves the capabilities of a printer driver.<br/>                                                                                                                                                                                                                                                       |
| [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc)<br/>                                         | The [**EndDoc**](https://msdn.microsoft.com/library/windows/desktop/dd162594) function ends a print job.<br/>                                                                                                                                                                                                                                                                                                             |
| [**EndPage**](/windows/desktop/api/Wingdi/nf-wingdi-endpage)<br/>                                       | The **EndPage** function notifies the device that the application has finished writing to a page. This function is typically used to direct the device driver to advance to a new page.<br/>                                                                                                                                                                             |
| [**Escape**](/windows/desktop/api/Wingdi/nf-wingdi-escape)<br/>                                         | enables an application to access the system-defined device capabilities that are not available through GDI.<br/>                                                                                                                                                                                                                                                         |
| [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape)<br/>                                   | The [**ExtEscape**](https://msdn.microsoft.com/library/windows/desktop/dd162708) function enables an application to access device capabilities that are not available through GDI.<br/>                                                                                                                                                                                                                                |
| [**IsWindowRedirectedForPrint**](iswindowredirectedforprint.md)<br/> | The [**IsWindowRedirectedForPrint**](iswindowredirectedforprint.md) function determines whether the specified window is currently redirected for printing.<br/>                                                                                                                                                                                                         |
| [**PrintWindow**](/windows/desktop/api/Winuser/nf-winuser-printwindow)<br/>                               | The [**PrintWindow**](https://msdn.microsoft.com/library/windows/desktop/dd162869) function copies a visual window into the specified device context (DC), typically a printer DC.<br/>                                                                                                                                                                                                                              |
| [**SetAbortProc**](/windows/desktop/api/Wingdi/nf-wingdi-setabortproc)<br/>                             | The [**SetAbortProc**](https://msdn.microsoft.com/library/windows/desktop/dd162960) function sets the application-defined abort function that allows a print job to be canceled during spooling.<br/>                                                                                                                                                                                                               |
| [**StartDoc**](/windows/desktop/api/Wingdi/nf-wingdi-startdoca)<br/>                                     | The [**StartDoc**](https://msdn.microsoft.com/library/windows/desktop/dd145114) function starts a print job.<br/>                                                                                                                                                                                                                                                                                                       |
| [**StartPage**](/windows/desktop/api/Wingdi/nf-wingdi-startpage)<br/>                                   | The [**StartPage**](https://msdn.microsoft.com/library/windows/desktop/dd145116) function prepares the printer driver to accept data.<br/>                                                                                                                                                                                                                                                                             |



 

 

 




