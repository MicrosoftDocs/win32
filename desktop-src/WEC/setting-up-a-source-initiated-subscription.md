---
title: Setting up a Source Initiated Subscription
description: Source-initiated subscriptions allow you to define a subscription on an event collector computer without defining the event source computers, and then multiple remote event source computers can be set up (using a group policy setting) to forward events to the event collector computer.
ms.assetid: c02b5075-d685-44cf-937f-a1edfd2550ca
ms.tgt_platform: multiple
ms.topic: article
ms.date: 12/17/2018
---

# Setting up a Source Initiated Subscription

Source-initiated subscriptions allow you to define a subscription on an event collector computer without defining the event source computers, and then multiple remote event source computers can be set up (using a group policy setting) to forward events to the event collector computer. This differs from a collector initiated subscription because in the collector initiated subscription model, the event collector must define all the event sources in the event subscription.

When setting up a source-initiated subscription, consider whether the event source computers are in the same domain as the event collector computer. The following sections describe the steps to follow when the event sources are in the same domain or not in the same domain as the event collector computer.

> [!Note]  
> Any computer in a domain, local or remote, can be an event collector. However, when choosing an event collector, it is important to select a machine that is topologically close to where the majority of the events will be generated. Sending events to a machine at a distant network location on a WAN can reduce overall performance and efficiency in event collection.

## Setting up a source-initiated subscription where the event sources are in the same domain as the event collector computer

Both the event source computers and the event collector computer must be configured to set up a source initiated subscription.

> [!Note]  
> These instructions assume that you have administrator access to the Windows Server domain controller serving the domain in which the remote computer or computers will be configured to collect events.

### Configuring the event source computer

1. Run the following command from an elevated privilege command prompt on the Windows Server domain controller to configure Windows Remote Management:

    **winrm qc -q**

2. Start group policy by running the following command:

    **%SYSTEMROOT%\\System32\\gpedit.msc**

3. Under the **Computer Configuration** node, expand the **Administrative Templates** node, then expand the **Windows Components** node, then select the **Event Forwarding** node.

4. Right-click the **SubscriptionManager** setting, and select **Properties**. Enable the **SubscriptionManager** setting, and click the **Show** button to add a server address to the setting. Add at least one setting that specifies the event collector computer. The **SubscriptionManager Properties** window contains an **Explain** tab that describes the syntax for the setting.

5. After the **SubscriptionManager** setting has been added, run the following command to ensure the policy is applied:

    **gpupdate /force**

### Configuring the event collector computer

1. Run the following command from an elevated privilege command prompt on the Windows Server domain controller to configure Windows Remote Management:

    **winrm qc -q**

2. Run the following command to configure the Event Collector service:

    **wecutil qc /q**

3. Create a source initiated subscription. This can either be done programmatically, by using the Event Viewer, or by using [**Wecutil.exe**](wecutil.md). For more information about how to create the subscription programmatically, see the code example in [Creating a Source Initiated Subscription](creating-a-source-initiated-subscription.md). If you use Wecutil.exe, you must create an event subscription XML file and use the following command:

    **wecutil cs** *configurationFile.xml*

    The following XML is an example of the contents of a subscription configuration file that creates a source-initiated subscription to forward events from the Application event log of a remote computer to the ForwardedEvents log on the event collector computer.

    ```XML
    <Subscription xmlns="http://schemas.microsoft.com/2006/03/windows/events/subscription">
        <SubscriptionId>SampleSISubscription</SubscriptionId>
        <SubscriptionType>SourceInitiated</SubscriptionType>
        <Description>Source Initiated Subscription Sample</Description>
        <Enabled>true</Enabled>
        <Uri>http://schemas.microsoft.com/wbem/wsman/1/windows/EventLog</Uri>

        <!-- Use Normal (default), Custom, MinLatency, MinBandwidth -->
        <ConfigurationMode>Custom</ConfigurationMode>

        <Delivery Mode="Push">
            <Batching>
                <MaxItems>1</MaxItems>
                <MaxLatencyTime>1000</MaxLatencyTime>
            </Batching>
            <PushSettings>
                <Heartbeat Interval="60000"/>
            </PushSettings>
        </Delivery>

        <Expires>2018-01-01T00:00:00.000Z</Expires>

        <Query>
            <![CDATA[
                <QueryList>
                    <Query Path="Application">
                        <Select>Event[System/EventID='999']</Select>
                    </Query>
                </QueryList>
            ]]>
        </Query>

        <ReadExistingEvents>true</ReadExistingEvents>
        <TransportName>http</TransportName>
        <ContentFormat>RenderedText</ContentFormat>
        <Locale Language="en-US"/>
        <LogFile>ForwardedEvents</LogFile>
        <AllowedSourceNonDomainComputers></AllowedSourceNonDomainComputers>
        <AllowedSourceDomainComputers>O:NSG:NSD:(A;;GA;;;DC)(A;;GA;;;NS)</AllowedSourceDomainComputers>
    </Subscription>
    ```

    > [!Note]  
    > When creating a source initiated subscription, if AllowedSourceDomainComputers, AllowedSourceNonDomainComputers/IssuerCAList, AllowedSubjectList, and DeniedSubjectList are all empty, then "O:NSG:NSD:(A;;GA;;;DC)(A;;GA;;;NS)" will be used as the default security descriptor for AllowedSourceDomainComputers. The default descriptor grants members of the Domain Computers domain group, as well as the local Network Service group (for the local forwarder), the ability to raise events for this subscription.

### To validate that the subscription works correctly

1. On the event collector computer complete the following steps:

    1. Run the following command from an elevated privilege command prompt on the Windows Server domain controller to get the runtime status of the subscription:

        **wecutil gr** *&lt;subscriptionID&gt;*

    2. Verify that the event source has connected. You might need to wait until the refresh interval specified in the policy is over after you create the subscription for the event source to be connected.
    3. Run the following command to get the subscription information:

        **wecutil gs** *&lt;subscriptionID&gt;*

    4. Get the DeliveryMaxItems value from the subscription information.

2. On the event source computer, raise the events that match the query from the event subscription. The DeliveryMaxItems number of events must be raised for the events to be forwarded.
3. On the event collector computer, validate that the events have been forwarded to the ForwardedEvents log or to the log specified in the subscription.

## Forwarding the security log

To be able to forward the Security log you need to add the NETWORK SERVICE account to the EventLog Readers group.

## Setting up a source initiated subscription where the event sources are not in the same domain as the event collector computer

> [!Note]  
> These instructions assume that you have administrator access to a Windows Server domain controller. In this case, since the remote event collector computer or computer(s) are not in the domain served by the domain controller, it is essential to start an individual client by setting Windows Remote Management to "automatic" using Services (services.msc). Alternatively, you can run "winrm quickconfig" on each remote client.

The following prerequisites must be met before the subscription is created.

1. On the event collector computer, run the following commands from an elevated privilege command prompt to configure Windows Remote Management and the Event Collector service:

    **winrm qc -q**

    **wecutil qc /q**

2. The collector computer should have a server authentication certificate (certificate with a server authentication purpose) in a local computer certificate store.
3. On the event source computer, run the following command to configure Windows Remote Management:

    **winrm qc -q**

4. The source machine should have a client authentication certificate (certificate with a client authentication purpose) in a local computer certificate store .
5. Port 5986 is opened on the event collector computer. To open this port, run the command:

    **netsh firewall add portopening TCP 5986 "Winrm HTTPS Remote Management"**

### Certificates requirements

- A server authentication certificate has to be installed on the Event Collector computer in the Personal store of the Local machine. The subject of this certificate has to match the FQDN of the collector.
- A client authentication certificate has to be installed on the Event Source computers in the Personal store of the Local machine. The subject of this certificate has to match the FQDN of the computer.
- If the client certificate has been issued by a different Certification Authority than the one of the Event Collector then those Root and Intermediate certificates needs to be installed on the Event Collector as well.
- If the client certificate was issued by an Intermediate certification authority and the collector is running Windows 2012 or later you will have to configure the following registry key:

    **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\Schannel\ClientAuthTrustMode (DWORD) = 2**
 
- Verify that both the server and client are able to successfully check revocation status on all certificates. Use of the **certutil** command can assist in troubleshooting any errors.

Find more information in this article: https://technet.microsoft.com/library/dn786429(v=ws.11).aspx

### Setup the listener on the Event collector

1. Set the certificate authentication with the following command:

    **winrm set winrm/config/service/auth @{Certificate="true"}**

2. A WinRM HTTPS listener with the server authentication certificate thumb print should exist on the event collector computer. This can be verified with the following command:

    **winrm e winrm/config/listener**

3. If you do not see the HTTPS listener, or if the HTTPS listener's thumb print is not same as the thumb print of the server authentication certificate on collector computer, then you can delete that listener and create a new one with the correct thumb print. To delete the https listener, use the following command:

    **winrm delete winrm/config/Listener?Address=*+Transport=HTTPS**

    To create a new listener, use the following command:

    **winrm create winrm/config/Listener?Address=&#42;+Transport=HTTPS @{Hostname="**&lt;_FQDN of the collector_&gt;**";CertificateThumbprint="**&lt;_Thumb print of the server authentication certificate_&gt;**"}**

### Configure certificate mapping on the Event Collector

1. Create new local user and add it to the local Administrators group.
2. Create the certificate mapping using a certificate that is present in the machine’s “Trusted Root Certification Authorities” or “Intermediate Certification Authorities”.

    This is the certificate of the Root or Intermediate CA that issued the certificates installed on the Event Source computers *(to avoid confusion, this is the CA immediately above the certificate in the certificate chain)*:

    **winrm create winrm/config/service/certmapping?Issuer**=&lt;_Thumbprint of the issuing CA certificate_&gt;**+Subject=&#42;+URI=&#42; @{UserName="**&lt;_username_&gt;**";Password="**&lt;_password_&gt;**"} -remote:localhost**

3. From a client test the listener and the certificate mapping with the following command:

    **winrm g winrm/config -r:https://**&lt;_Event Collector FQDN_&gt;**:5986 -a:certificate -certificate:"**&lt;_Thumbprint of the client authentication certificate_&gt;**"**

    This should return the WinRM configuration of the Event collector. **Do not** move past this step if the configuration is not displayed.

    **What happens at this step?**
    - The client connects to the Event Collector and sends the specified certificate
    - The Event Collector looks for the issuing CA and checks if the is a matching certificate mapping
    - The Event Collector validates the client certificate chain and revocations status
    - If the above steps succeeds the authentication is completed.

> [!NOTE]
> You might get an Access denied error complaining about the authentication method, which could be misleading. To troubleshoot, check the CAPI log on the Event Collector.

4. List the configured certmapping entries with the command:
  **winrm enum winrm/config/service/certmapping**

### Event Source computer Configuration

1. Logon with an administrator account and open the Local Group Policy Editor (gpedit.msc)
2. Navigate to the Local Computer Policy\Computer Configuration\Administrative Templates\Windows Components\Event Forwarding.
3. Open “Configure the server address, refresh interval, and issuer certificate authority of a target Subscription Manager” policy.
4. Enable the policy and click the SubscriptionManagers “Show...” button.
5. In the SubscriptionManagers window enter the following string:

    **Server=HTTPS://**&lt;_FQDN of the Event Collector server_&gt;**:5986/wsman/SubscriptionManager/WEC,Refresh=** &lt;_Refresh interval in seconds_&gt;**,IssuerCA=**&lt;_Thumbprint of the issuing CA certificate_&gt;

6. Run the following command line to refresh Local Group Policy settings:Gpupdate /force
7. These steps should produce event 104 in your source computer Event Viewer Applications and Services Logs\Microsoft\Windows\Eventlog-ForwardingPlugin\Operational log with the following message:

    "The forwarder has successfully connected to the subscription manager at address &lt;FQDN&gt;followed by event 100 with the message: "The subscription &lt;sub_name&gt; is created successfully."

8. On the Event Collector, the Subscription Runtime Status will show now 1 Active computer.
9. Open the ForwardedEvents log on the Event Collector and check if you have the events forwarded from the Source computers.

### Grant permission on the private key of the client certificate on the Event Source

1. Open the Certificates management console for Local machine on the Event Source computer.
2. Right click on the client certificate then Manage Private keys.
3. Grant Read permission to the NETWORK SERVICE user.

### Event subscription configuration

1. Open Event Viewer in the Event Collector and navigate to the Subscriptions node.
2. Right-click Subscriptions and choose “Create Subscription…”
3. Give a name and an optional description for the new Subscription.
4. Select “Source computer initiated” option and click “Select Computer Groups…”.
5. In Computer Groups click on “Add Non-Domain Computers…” and type the event source hostname.
6. Click “Add Certificates…” and add the certificate of the Certification authority that issue the client certificates. You can click in View Certificate to validate the certificate.
7. In Certificate Authorities click OK to add the certificate.
8. When finished adding Computers click OK.
9. Back to the Subscription Properties, click in Select Events...
10. Configure the Events Query Filter by specifying the event level(s), event log(s) or event source(s), the event ID(s) and any other filtering options.
11. Back to the Subscription Properties, click on Advanced...
12. Choose one of the optimization options for event delivery from the Source Event to the Event Collector, or leave the default Normal: 
    1. **Minimize Bandwidth**: Events will be delivered will less frequency to save bandwidth.
    2. **Minimize Latency**: Events will be delivered as soon as they occur to reduce events latency.
13. Change the Protocol to HTTPS and click OK.
14. Click OK to create the new subscription.
15. Check the runtime status of the Subscription by right-clicking and choosing “Runtime Status”
