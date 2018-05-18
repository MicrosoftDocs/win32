---
title: Frequently Asked Questions
description: The following questions and answers cover the most frequently encountered Windows Firewall situations.
ms.assetid: '83febda0-e6b0-425a-9686-40dca1591ea7'
---

# Frequently Asked Questions

The following questions and answers cover the most frequently encountered Windows Firewall situations.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Question</th>
<th>Answer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>How is the Windows Firewall MMC snap-in accessed from the command line?</td>
<td>Type &quot;mmc WF.msc&quot; to launch the firewall MMC snap-in.</td>
</tr>
<tr class="even">
<td>How can the currently active Windows Firewall profile be determined?</td>
<td>The simplest way to find out which is the currently active profile is to open the Windows Firewall MMC snap-in and look at the main page visible on startup.<br/> Alternatively, it can also be determined from the command line using &quot;netsh advfirewall&gt;show currentprofile&quot;, or by accessing the Windows Firewall section of the Control Panel.<br/></td>
</tr>
<tr class="odd">
<td>How can it be determined if the firewall is on?</td>
<td>Open the Firewall MMC snap-in and look at the main page visible on startup. It shows the firewall state for the Domain, Public and Private profiles.<br/> Alternatively, the status of the firewall can be checked from the command line using &quot;netsh advfirewall&gt;show allprofiles&quot;, or by accessing the Windows Firewall section of the Control Panel.<br/></td>
</tr>
<tr class="even">
<td>How can inbound filtering be enabled for the firewall?</td>
<td>Open the Firewall MMC snap-in and look at the main page visible on startup. <br/> At the bottom of the Overview section, click &quot;Windows Firewall Properties&quot;.<br/> For each Domain, Private, and Public profile tab change the firewall state from &quot;Off&quot; to &quot;On (recommended)&quot;.<br/> Alternatively, inbound filtering for the firewall can be enabled for all profiles by using the following command: &quot;netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound&quot;<br/></td>
</tr>
<tr class="odd">
<td>How can the firewall be enabled for a specific adapter?</td>
<td>Follow these steps:<br/>
<ol>
<li>Open the Windows Firewall Control Panel.</li>
<li>Click the Windows Firewall Settings link.</li>
<li>Switch to the &quot;Advanced&quot; tab.</li>
<li>The &quot;Network Connections&quot; shows a list of the adapters available on the machine.</li>
<li>Check the box for each adapter where the firewall needs to be enabled.</li>
</ol></td>
</tr>
<tr class="even">
<td>Traffic that was expected to get blocked (or allowed) did not. What can be done to ensure that expected behavior occurs?</td>
<td>Follow the steps below. If at any point you answer &quot;No&quot; to any of the questions, this is where you need to focus your attention to resolve the problem.<br/> Are the following services running? If so, continue.<br/>
<ul>
<li>Base Filtering Engine</li>
<li>Group Policy Client</li>
<li>IKE and AuthIP IPsec Keying Modules</li>
<li>IP Helper</li>
<li>IPsec</li>
<li>Network Location Awareness</li>
<li>Windows Firewall</li>
<li>Windows Firewall Authorization Driver</li>
<li>Network List Service</li>
</ul>
Is the firewall on? If so, continue.<br/> In a command line window type &quot;Ipconfig&quot;.<br/> Get the adapter of the local address you used to receive the connection. This is the adapter you used for your connection.<br/> Is the firewall enabled on the adapter you used for you connection? If so, continue.<br/>
<ol>
<li>Open the Windows Firewall MMC console.</li>
<li>Under &quot;Windows Firewall With Advanced Security&quot;, click the &quot;Inbound Rules&quot; node or on the &quot;Outbound Rules&quot; node as appropriate.</li>
<li>By sorting the columns visible in the rule list such as &quot;Program&quot;, &quot;Local / Remote Address&quot;, &quot;Local/Remote Port&quot;, &quot;Protocol&quot;, &quot;Direction&quot;, find the rules that closely match the connection which should have been handled by the firewall.</li>
<li>For each rule that you have identified as a close candidate, make sure that the following rule attributes are true:
<ul>
<li>The rule is active</li>
<li>The rule is configured to block (or allow traffic as appropriate)</li>
<li>The rule is referencing the proper program path for the application</li>
<li>If the application is a service, make sure that the service list is properly scoped.</li>
<li>That the addresses, subnet, ports and protocols are correct for the traffic you want to handle.</li>
<li>That the traffic direction is correct.</li>
<li>The profiles associated with the rule are missing or incorrect.</li>
</ul></li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 





