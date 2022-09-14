---
description: The functions in this section install and configure printer drivers on a computer.
ms.assetid: e6aa8963-aa1a-4313-bc24-2aeb4f4b93c4
title: Printer Driver Installation Reference
ms.topic: article
ms.date: 05/31/2018
---

# Printer Driver Installation Reference

The functions in this section install and configure printer drivers on a computer.

## In this section




| Function | Description | 
|----------|-------------|
| <a href="addmonitor.md"><strong>AddMonitor</strong></a><br /> | The <a href="/windows/desktop/printdocs/addmonitor"><strong>AddMonitor</strong></a> function installs a local port monitor and links the configuration, data, and monitor files.<br /> | 
| <a href="addport.md"><strong>AddPort</strong></a><br /> | The <a href="/windows/desktop/printdocs/addport"><strong>AddPort</strong></a> function adds the name of a port to the list of supported ports. The <strong>AddPort</strong> function is exported by the port monitor.<br /> | 
| <a href="addprinterdriver.md"><strong>AddPrinterDriver</strong></a><br /> | The <a href="/windows/desktop/printdocs/addprinterdriver"><strong>AddPrinterDriver</strong></a> function installs a local or remote printer driver and associates the configuration, data, and driver files.<br /> For more flexibility in installing or upgrading printer drivers, use the <a href="addprinterdriverex.md"><strong>AddPrinterDriverEx</strong></a> function because it allows strict upgrade, strict downgrade, copying of newer files only, and copying of all files (regardless of the file time stamps).<br /><blockquote>[!Note]<br />Installing a printer driver without a driver package is no longer recommended. Use <a href="installprinterdriverfrompackage.md"><strong>InstallPrinterDriverFromPackage</strong></a> instead.</blockquote><br /> | 
| <a href="addprinterdriverex.md"><strong>AddPrinterDriverEx</strong></a><br /> | The <a href="/windows/desktop/printdocs/addprinterdriverex"><strong>AddPrinterDriverEx</strong></a> function installs a local or remote printer driver and links the configuration, data, and driver files. Besides having the capabilities of <a href="addprinterdriver.md"><strong>AddPrinterDriver</strong></a>, it also has options that permit strict upgrade, strict downgrade, copying of newer files only, and copying of all files (regardless of file time stamps).<br /><blockquote>[!Note]<br />Installing a printer driver without a driver package is no longer recommended. Use <a href="installprinterdriverfrompackage.md"><strong>InstallPrinterDriverFromPackage</strong></a> instead.</blockquote><br /> | 
| <a href="addprintprocessor.md"><strong>AddPrintProcessor</strong></a><br /> | The <a href="/windows/desktop/printdocs/addprintprocessor"><strong>AddPrintProcessor</strong></a> function installs a print processor on the specified server and adds the print-processor name to the list of supported print processors.<br /> | 
| <a href="addprintprovidor.md"><strong>AddPrintProvidor</strong></a><br /> | The <a href="/windows/desktop/printdocs/addprintprovidor"><strong>AddPrintProvidor</strong></a> function installs a local print provider and links the configuration, data, and provider files.<br /> | 
| <a href="coreprinterdriverinstalled.md"><strong>CorePrinterDriverInstalled</strong></a><br /> | The <a href="/windows/desktop/printdocs/coreprinterdriverinstalled"><strong>CorePrinterDriverInstalled</strong></a> function reports whether a core printer driver with a specified GUID, date, and version is installed.<br /> | 
| <a href="deletemonitor.md"><strong>DeleteMonitor</strong></a><br /> | The <a href="/windows/desktop/printdocs/deletemonitor"><strong>DeleteMonitor</strong></a> function removes a port monitor added by the <a href="addmonitor.md"><strong>AddMonitor</strong></a> function.<br /> | 
| <a href="deleteport.md"><strong>DeletePort</strong></a><br /> | The <a href="/windows/desktop/printdocs/deleteport"><strong>DeletePort</strong></a> function displays a dialog box that allows the user to delete a port name.<br /> | 
| <a href="deleteprinterdriver.md"><strong>DeletePrinterDriver</strong></a><br /> | The <a href="/windows/desktop/printdocs/deleteprinterdriver"><strong>DeletePrinterDriver</strong></a> function removes the specified printer-driver name from the list of names of supported drivers on a server.<br /> To delete the files associated with the driver in addition to removing the specified printer-driver name from the list of names of supported drivers for a server, use the <a href="deleteprinterdriverex.md"><strong>DeletePrinterDriverEx</strong></a> function.<br /><a href="/windows/desktop/printdocs/deleteprinterdriver"><strong>DeletePrinterDriver</strong></a> deletes a driver only if no version of the driver is in use for the specified environment. <a href="deleteprinterdriverex.md"><strong>DeletePrinterDriverEx</strong></a> can delete specific versions of the driver.<br /> | 
| <a href="deleteprinterdriverex.md"><strong>DeletePrinterDriverEx</strong></a><br /> | The <a href="/windows/desktop/printdocs/deleteprinterdriverex"><strong>DeletePrinterDriverEx</strong></a> function removes the specified printer-driver name from the list of names of supported drivers on a server and deletes the files associated with the driver. This function can also delete specific versions of the driver.<br /> | 
| <a href="deleteprinterdriverpackage.md"><strong>DeletePrinterDriverPackage</strong></a><br /> | Deletes a printer driver package from the driver store.<br /> | 
| <a href="deleteprintprocessor.md"><strong>DeletePrintProcessor</strong></a><br /> | The <a href="/windows/desktop/printdocs/deleteprintprocessor"><strong>DeletePrintProcessor</strong></a> function removes a print processor added by the <a href="addprintprocessor.md"><strong>AddPrintProcessor</strong></a> function.<br /> | 
| <a href="deleteprintprovidor.md"><strong>DeletePrintProvidor</strong></a><br /> | The <a href="/windows/desktop/printdocs/deleteprintprovidor"><strong>DeletePrintProvidor</strong></a> function removes a print provider added by the <a href="addprintprovidor.md"><strong>AddPrintProvidor</strong></a> function.<br /> | 
| <a href="enummonitors.md"><strong>EnumMonitors</strong></a><br /> | The <a href="/windows/desktop/printdocs/enummonitors"><strong>EnumMonitors</strong></a> function retrieves information about the port monitors installed on the specified server.<br /> | 
| <a href="enumports.md"><strong>EnumPorts</strong></a><br /> | The <a href="/windows/desktop/printdocs/enumports"><strong>EnumPorts</strong></a> function enumerates the ports that are available for printing on a specified server.<br /> | 
| <a href="enumprinterdrivers.md"><strong>EnumPrinterDrivers</strong></a><br /> | The <a href="/windows/desktop/printdocs/enumprinterdrivers"><strong>EnumPrinterDrivers</strong></a> function enumerates the printer drivers installed on a specified printer server.<br /> | 
| <a href="enumprintprocessordatatypes.md"><strong>EnumPrintProcessorDatatypes</strong></a><br /> | The <a href="/windows/desktop/printdocs/enumprintprocessordatatypes"><strong>EnumPrintProcessorDatatypes</strong></a> function enumerates the data types that a specified print processor supports.<br /> | 
| <a href="enumprintprocessors.md"><strong>EnumPrintProcessors</strong></a><br /> | The <a href="/windows/desktop/printdocs/enumprintprocessors"><strong>EnumPrintProcessors</strong></a> function enumerates the print processors installed on the specified server.<br /> | 
| <a href="getcoreprinterdrivers.md"><strong>GetCorePrinterDrivers</strong></a><br /> | Retrieves GUID, version, and date of the specified core printer drivers and the path to their packages.<br /> | 
| <a href="getprinterdriver.md"><strong>GetPrinterDriver</strong></a><br /> | The <a href="/windows/desktop/printdocs/getprinterdriver"><strong>GetPrinterDriver</strong></a> function retrieves driver data for the specified printer. If the driver is not installed on the local computer, <strong>GetPrinterDriver</strong> installs it.<br /> | 
| <a href="getprinterdriver2.md"><strong>GetPrinterDriver2</strong></a><br /> | The <a href="getprinterdriver2.md"><strong>GetPrinterDriver2</strong></a> function retrieves driver data for the specified printer. If the driver is not installed on the local computer, <strong>GetPrinterDriver2</strong> installs it and displays any user interface to the specified window.<br /> | 
| <a href="getprinterdriverdirectory.md"><strong>GetPrinterDriverDirectory</strong></a><br /> | The <a href="/windows/desktop/printdocs/getprinterdriverdirectory"><strong>GetPrinterDriverDirectory</strong></a> function retrieves the path of the printer-driver directory.<br /> | 
| <a href="getprinterdriverpackagepath.md"><strong>GetPrinterDriverPackagePath</strong></a><br /> | Retrieves the path to the specified printer driver package on a print server.<br /> | 
| <a href="getprintprocessordirectory.md"><strong>GetPrintProcessorDirectory</strong></a><br /> | The <a href="/windows/desktop/printdocs/getprintprocessordirectory"><strong>GetPrintProcessorDirectory</strong></a> function retrieves the path to the print processor directory on the specified server.<br /> | 
| <a href="installprinterdriverfrompackage.md"><strong>InstallPrinterDriverFromPackage</strong></a><br /> | Installs a printer driver from a driver package that is in the print server's driver store.<br /> | 
| <a href="uploadprinterdriverpackage.md"><strong>UploadPrinterDriverPackage</strong></a><br /> | Uploads a printer driver to the print server's driver store so that it can be installed by calling <a href="installprinterdriverfrompackage.md"><strong>InstallPrinterDriverFromPackage</strong></a>.<br /> | 




 

 

