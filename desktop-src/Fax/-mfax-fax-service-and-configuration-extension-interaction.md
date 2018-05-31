---
Description: The following diagram shows the interaction between the fax service and a fax extension DLL if the extension DLL exports the FaxExtInitializeConfig function. The numbers in the diagram refer to the event numbers in the table that follows the diagram.
ms.assetid: 93d91987-a904-428d-97d9-dd4894d98f13
title: Fax Service and Configuration Extension Interaction
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Service and Configuration Extension Interaction

The following diagram shows the interaction between the fax service and a fax extension DLL if the extension DLL exports the [**FaxExtInitializeConfig**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextinitializeconfig) function. The numbers in the diagram refer to the event numbers in the table that follows the diagram.

> [!Note]  
> With the exception of Event 1, the numbered events in the following diagram do not imply a sequence of steps or the order in which the function calls must occur. The numbers relate only to the events in the table that follows the diagram.

 

![interaction between the fax service and a fax extension dll if the dll exports faxextinitializeconfig](images/faxser.png)

The following table lists the primary events that can occur if you use the fax extension configuration API to retrieve and set fax device configuration data.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Except in the case of a virtual fax service provider (FSP), the fax service calls the [<strong>FaxExtInitializeConfig</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextinitializeconfig) function before it calls the extension's general initialization routine. In the case of a virtual FSP, the fax service calls [<strong>FaxDevVirtualDeviceCreation</strong>](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevvirtualdevicecreation) before it calls <strong>FaxExtInitializeConfig</strong>. <strong>FaxExtInitializeConfig</strong> passes pointers to the fax service's callback functions. The extension DLL must store the pointers.<br/></td>
</tr>
<tr class="even">
<td>2</td>
<td>To retrieve configuration data, the extension DLL must call the fax service's [<strong>FaxExtGetData</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextgetdata) callback function, using the callback function pointer provided by the fax service in Event 1. The fax service allocates any memory required for the data and returns the information to the fax extension.<br/> For more information, see Event 6.<br/></td>
</tr>
<tr class="odd">
<td>3</td>
<td>To register to receive notifications about configuration data changes, the extension DLL must call the fax service's [<strong>FaxExtRegisterForEvents</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextregisterforevents) callback function. (The fax service provides a pointer to this callback function in Event 1.) When you call <strong>FaxExtRegisterForEvents</strong>, you must supply the pointer to a [<strong>FaxExtConfigChange</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextconfigchange) callback routine that you implement. The fax service calls this routine to send notifications to the extension.<br/> For more information, see Event 7.<br/></td>
</tr>
<tr class="even">
<td>4</td>
<td>To set configuration data, the extension DLL must call the fax service's [<strong>FaxExtSetData</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextsetdata) callback function, using the callback function pointer provided by the fax service in Event 1.<br/></td>
</tr>
<tr class="odd">
<td>5</td>
<td>To stop receiving notifications about configuration data changes (after registering for notifications as outlined in Event 3), the extension DLL can unregister by calling the fax service's [<strong>FaxExtUnregisterForEvents</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextunregisterforevents) callback function, using the callback function pointer provided by the fax service in Event 1.<br/></td>
</tr>
<tr class="even">
<td>6</td>
<td>If the extension DLL previously called the [<strong>FaxExtGetData</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextgetdata) function, the extension must deallocate the data after it processes the data returned in Event 2.<br/>
<blockquote>
[!Note]<br />
The extension must deallocate the data by calling the fax service's [<strong>FaxExtFreeBuffer</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextfreebuffer) callback function, using the callback function pointer provided by the fax service in Event 1.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>7</td>
<td>If the extension DLL previously registered to receive notifications about configuration data changes (as in Event 3), the fax service notifies the extension by calling the extension's [<strong>FaxExtConfigChange</strong>](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextconfigchange) callback function.<br/></td>
</tr>
</tbody>
</table>



 

Examples of instances when the fax service might send configuration change notifications include when another extension sets a new value for a device and data GUID for which the extension DLL has already set a value.

 

 




