---
Description: The functions in this section install and configure printer drivers on a computer.
ms.assetid: e6aa8963-aa1a-4313-bc24-2aeb4f4b93c4
title: Printer Driver Installation Reference
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Printer Driver Installation Reference

The functions in this section install and configure printer drivers on a computer.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>AddMonitor</strong>](addmonitor.md)<br/></td>
<td>The [<strong>AddMonitor</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183341) function installs a local port monitor and links the configuration, data, and monitor files.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AddPort</strong>](addport.md)<br/></td>
<td>The [<strong>AddPort</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183342) function adds the name of a port to the list of supported ports. The <strong>AddPort</strong> function is exported by the port monitor.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>AddPrinterDriver</strong>](addprinterdriver.md)<br/></td>
<td>The [<strong>AddPrinterDriver</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183346) function installs a local or remote printer driver and associates the configuration, data, and driver files.<br/> For more flexibility in installing or upgrading printer drivers, use the [<strong>AddPrinterDriverEx</strong>](addprinterdriverex.md) function because it allows strict upgrade, strict downgrade, copying of newer files only, and copying of all files (regardless of the file time stamps).<br/>
<blockquote>
[!Note]<br />
Installing a printer driver without a driver package is no longer recommended. Use [<strong>InstallPrinterDriverFromPackage</strong>](installprinterdriverfrompackage.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>AddPrinterDriverEx</strong>](addprinterdriverex.md)<br/></td>
<td>The [<strong>AddPrinterDriverEx</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183347) function installs a local or remote printer driver and links the configuration, data, and driver files. Besides having the capabilities of [<strong>AddPrinterDriver</strong>](addprinterdriver.md), it also has options that permit strict upgrade, strict downgrade, copying of newer files only, and copying of all files (regardless of file time stamps).<br/>
<blockquote>
[!Note]<br />
Installing a printer driver without a driver package is no longer recommended. Use [<strong>InstallPrinterDriverFromPackage</strong>](installprinterdriverfrompackage.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>AddPrintProcessor</strong>](addprintprocessor.md)<br/></td>
<td>The [<strong>AddPrintProcessor</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183348) function installs a print processor on the specified server and adds the print-processor name to the list of supported print processors.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AddPrintProvidor</strong>](addprintprovidor.md)<br/></td>
<td>The [<strong>AddPrintProvidor</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183349) function installs a local print provider and links the configuration, data, and provider files.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CorePrinterDriverInstalled</strong>](coreprinterdriverinstalled.md)<br/></td>
<td>The [<strong>CorePrinterDriverInstalled</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183482) function reports whether a core printer driver with a specified GUID, date, and version is installed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeleteMonitor</strong>](deletemonitor.md)<br/></td>
<td>The [<strong>DeleteMonitor</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183538) function removes a port monitor added by the [<strong>AddMonitor</strong>](addmonitor.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeletePort</strong>](deleteport.md)<br/></td>
<td>The [<strong>DeletePort</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183540) function displays a dialog box that allows the user to delete a port name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeletePrinterDriver</strong>](deleteprinterdriver.md)<br/></td>
<td>The [<strong>DeletePrinterDriver</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183545) function removes the specified printer-driver name from the list of names of supported drivers on a server.<br/> To delete the files associated with the driver in addition to removing the specified printer-driver name from the list of names of supported drivers for a server, use the [<strong>DeletePrinterDriverEx</strong>](deleteprinterdriverex.md) function.<br/> [<strong>DeletePrinterDriver</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183545) deletes a driver only if no version of the driver is in use for the specified environment. [<strong>DeletePrinterDriverEx</strong>](deleteprinterdriverex.md) can delete specific versions of the driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeletePrinterDriverEx</strong>](deleteprinterdriverex.md)<br/></td>
<td>The [<strong>DeletePrinterDriverEx</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183546) function removes the specified printer-driver name from the list of names of supported drivers on a server and deletes the files associated with the driver. This function can also delete specific versions of the driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeletePrinterDriverPackage</strong>](deleteprinterdriverpackage.md)<br/></td>
<td>Deletes a printer driver package from the driver store.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeletePrintProcessor</strong>](deleteprintprocessor.md)<br/></td>
<td>The [<strong>DeletePrintProcessor</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183549) function removes a print processor added by the [<strong>AddPrintProcessor</strong>](addprintprocessor.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeletePrintProvidor</strong>](deleteprintprovidor.md)<br/></td>
<td>The [<strong>DeletePrintProvidor</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183550) function removes a print provider added by the [<strong>AddPrintProvidor</strong>](addprintprovidor.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EnumMonitors</strong>](enummonitors.md)<br/></td>
<td>The [<strong>EnumMonitors</strong>](https://msdn.microsoft.com/library/windows/desktop/dd162631) function retrieves information about the port monitors installed on the specified server.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EnumPorts</strong>](enumports.md)<br/></td>
<td>The [<strong>EnumPorts</strong>](https://msdn.microsoft.com/library/windows/desktop/dd162687) function enumerates the ports that are available for printing on a specified server.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EnumPrinterDrivers</strong>](enumprinterdrivers.md)<br/></td>
<td>The [<strong>EnumPrinterDrivers</strong>](https://msdn.microsoft.com/library/windows/desktop/dd162690) function enumerates the printer drivers installed on a specified printer server.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EnumPrintProcessorDatatypes</strong>](enumprintprocessordatatypes.md)<br/></td>
<td>The [<strong>EnumPrintProcessorDatatypes</strong>](https://msdn.microsoft.com/library/windows/desktop/dd162693) function enumerates the data types that a specified print processor supports.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EnumPrintProcessors</strong>](enumprintprocessors.md)<br/></td>
<td>The [<strong>EnumPrintProcessors</strong>](https://msdn.microsoft.com/library/windows/desktop/dd162694) function enumerates the print processors installed on the specified server.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetCorePrinterDrivers</strong>](getcoreprinterdrivers.md)<br/></td>
<td>Retrieves GUID, version, and date of the specified core printer drivers and the path to their packages.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetPrinterDriver</strong>](getprinterdriver.md)<br/></td>
<td>The [<strong>GetPrinterDriver</strong>](https://msdn.microsoft.com/library/windows/desktop/dd144914) function retrieves driver data for the specified printer. If the driver is not installed on the local computer, <strong>GetPrinterDriver</strong> installs it.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetPrinterDriver2</strong>](getprinterdriver2.md)<br/></td>
<td>The [<strong>GetPrinterDriver2</strong>](getprinterdriver2.md) function retrieves driver data for the specified printer. If the driver is not installed on the local computer, <strong>GetPrinterDriver2</strong> installs it and displays any user interface to the specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetPrinterDriverDirectory</strong>](getprinterdriverdirectory.md)<br/></td>
<td>The [<strong>GetPrinterDriverDirectory</strong>](https://msdn.microsoft.com/library/windows/desktop/dd144915) function retrieves the path of the printer-driver directory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetPrinterDriverPackagePath</strong>](getprinterdriverpackagepath.md)<br/></td>
<td>Retrieves the path to the specified printer driver package on a print server.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetPrintProcessorDirectory</strong>](getprintprocessordirectory.md)<br/></td>
<td>The [<strong>GetPrintProcessorDirectory</strong>](https://msdn.microsoft.com/library/windows/desktop/dd144917) function retrieves the path to the print processor directory on the specified server.<br/></td>
</tr>
<tr class="even">
<td>[<strong>InstallPrinterDriverFromPackage</strong>](installprinterdriverfrompackage.md)<br/></td>
<td>Installs a printer driver from a driver package that is in the print server's driver store.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UploadPrinterDriverPackage</strong>](uploadprinterdriverpackage.md)<br/></td>
<td>Uploads a printer driver to the print server's driver store so that it can be installed by calling [<strong>InstallPrinterDriverFromPackage</strong>](installprinterdriverfrompackage.md).<br/></td>
</tr>
</tbody>
</table>



 

 

 




