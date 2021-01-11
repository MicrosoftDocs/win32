---
description: The FhManagew.exe program deletes file versions that exceed a specified age from the currently assigned File History target device.
ms.assetid: 31A6E1AC-492A-4080-9095-3180FD60A575
title: FhManagew.exe
ms.topic: article
ms.date: 05/31/2018
---

# FhManagew.exe

The FhManagew.exe program deletes file versions that exceed a specified age from the currently assigned File History target device.

This program is available in Windows 8 and Windows Server 2012 and later.

To execute this program, go to the **Start** menu, click **Run**, and type the following command.

**FhManagew.exe -cleanup** *age*



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="age"></span><span id="AGE"></span><em>age</em><br/></td>
<td>This parameter specifies the minimum age, in days, of file versions that can be deleted. A file version is deleted if both of the following conditions are true:<br/>
<ul>
<li>The file version is older than the specified age.</li>
<li>The file is no longer included in the protection scope, or there is a newer version of the same file on the target device.</li>
</ul>
If the <em>age</em> parameter is set to zero, all file versions are deleted, except for the newest version of each file that is currently present in the protection scope.<br/></td>
</tr>
</tbody>
</table>



 

To suppress all output from this program, use the **-quiet** command-line option as follows.

**FhManagew.exe -cleanup** *age* **-quiet**

## Examples



| Example                                                                                                                                                                                                      | Description                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <span id="FhManagew.exe_-cleanup_30"></span><span id="fhmanagew.exe_-cleanup_30"></span><span id="FHMANAGEW.EXE_-CLEANUP_30"></span>**FhManagew.exe -cleanup 30**<br/>                                 | Delete all file versions that are older than one month.<br/>                        |
| <span id="FhManagew.exe_-cleanup_365_-quiet"></span><span id="fhmanagew.exe_-cleanup_365_-quiet"></span><span id="FHMANAGEW.EXE_-CLEANUP_365_-QUIET"></span>**FhManagew.exe -cleanup 365 -quiet**<br/> | Delete all file versions that are older than one year and suppress all output.<br/> |



 

 

 




