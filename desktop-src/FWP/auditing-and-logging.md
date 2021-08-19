---
title: Auditing
description: Windows Filtering Platform (WFP) provides auditing of firewall and IPsec related events.
ms.assetid: 30ff9cf7-bf93-4979-bacd-d76e5dadbef6
ms.topic: article
ms.date: 05/31/2018
---

# Auditing

The Windows Filtering Platform (WFP) provides auditing of firewall and IPsec related events. These events are stored in the system security log.

The audited events are as follows.




| Auditing category | Auditing subcategory | Audited events | 
|-------------------|----------------------|----------------|
| Policy Change<br /> {6997984D-797A-11D9-BED3-505054503030}<br /> | Filtering Platform Policy Change<br /> {0CCE9233-69AE-11D9-BED3-505054503030}<br /> | <blockquote>[!Note]<br />The numbers represent the Event IDs as displayed by Event Viewer (eventvwr.exe).</blockquote><br /> WFP object addition and removal:<br /><ul><li>5440 Persistent callout added</li><li>5441 Boot-time or persistent filter added</li><li>5442 Persistent provider added</li><li>5443 Persistent provider context added</li><li>5444 Persistent sub-layer added</li><li>5446 Run-time callout added or removed</li><li>5447 Run-time filter added or removed</li><li>5448 Run-time provider added or removed</li><li>5449 Run-time provider context added or removed</li><li>5450 Run-time sub-layer added or removed</li></ul> | 
| Object Access<br /> {6997984A-797A-11D9-BED3-505054503030}<br /> | Filtering Platform Packet Drop <br /> {0CCE9225-69AE-11D9-BED3-505054503030}<br /> | Packets dropped by WFP:<br /><ul><li>5152 Packet dropped</li><li>5153 Packet vetoed</li></ul> | 
| Object Access<br /> | Filtering Platform Connection <br /> {0CCE9226-69AE-11D9-BED3-505054503030}<br /> | Allowed and blocked connections:<br /><ul><li>5154 Listen permitted</li><li>5155 Listen blocked</li><li>5156 Connection permitted</li><li>5157 Connection blocked</li><li>5158 Bind permitted</li><li>5159 Bind blocked</li></ul><blockquote>[!Note]<br />Permitted connections do not always audit the ID of the associated filter. The FilterID for TCP will be 0 unless a subset of these filtering conditions are used: UserID, AppID, Protocol, Remote Port.</blockquote><br /> | 
| Object Access<br /> | Other Object Access Events<br /> {0CCE9227-69AE-11D9-BED3-505054503030}<br /> | <blockquote>[!Note]<br />This subcategory enables many audits. WFP specific audits are listed below.</blockquote><br /> Denial of Service prevention status:<br /><ul><li>5148 WFP DoS prevention mode started</li><li>5149 WFP DoS prevention mode stopped</li></ul> | 
| Logon/Logoff<br /> {69979849-797A-11D9-BED3-505054503030}<br /> | IPsec Main Mode<br /> {0CCE9218-69AE-11D9-BED3-505054503030}<br /> | IKE and AuthIP Main Mode negotiation:<br /><ul><li>4650, 4651 Security association established</li><li>4652, 4653 Negotiation failed</li><li>4655 Security association ended</li></ul> | 
| Logon/Logoff<br /> | IPsec Quick Mode <br /> {0CCE9219-69AE-11D9-BED3-505054503030}<br /> | IKE and AuthIP Quick Mode negotiation:<br /><ul><li>5451 Security association established</li><li>5452 Security association ended</li><li>4654 Negotiation failed</li></ul> | 
| Logon/Logoff <br /> | IPsec Extended Mode<br /> {0CCE921A-69AE-11D9-BED3-505054503030}<br /> | AuthIP Extended Mode negotiation:<br /><ul><li>4978 Invalid negotiation packet</li><li>4979, 4980, 4981, 4982 Security association established</li><li>4983, 4984 Negotiation failed</li></ul> | 
| System<br /> {69979848-797A-11D9-BED3-505054503030}<br /> | IPsec Driver<br /> {0CCE9213-69AE-11D9-BED3-505054503030}<br /> | Packets dropped by the IPsec driver:<br /><ul><li>4963 Inbound clear text packet dropped</li></ul> | 




 

By default, auditing for WFP is disabled.

Auditing can be enabled on a per-category basis through either the Group Policy Object Editor MMC snap-in, the Local Security Policy MMC snap-in, or the auditpol.exe command.

For example, to enable the auditing of Policy Change events you may:

-   Use the Group Policy Object Editor

    1.  Run **gpedit.msc**.
    2.  Expand Local Computer Policy.
    3.  Expand Computer Configuration.
    4.  Expand Windows Settings.
    5.  Expand Security Settings.
    6.  Expand Local Policies.
    7.  Click Audit Policy.
    8.  Double-click Audit policy change in order to launch the Properties dialog box.
    9.  Check the Success and Failure check-boxes.

-   Use the Local Security Policy

    1.  Run **secpol.msc**.
    2.  Expand Local Policies.
    3.  Click Audit Policy.
    4.  Double-click Audit policy change in order to launch the Properties dialog box.
    5.  Check the Success and Failure check-boxes.

-   Use the auditpol.exe command

    -   **auditpol /set /category:"Policy Change" /success:enable /failure:enable**

Auditing can be enabled on a per-subcategory basis only through the auditpol.exe command.

The auditing category and subcategory names are localized. To avoid localization for auditing scripts, the corresponding GUIDs may be used in place of the names.

For example, to enable the auditing of Filtering Platform Policy Change events you may use either one of the following commands:

-   **auditpol /set /subcategory:"Filtering Platform Policy Change" /success:enable /failure:enable**
-   **auditpol /set /subcategory:"{0CCE9233-69AE-11D9-BED3-505054503030}" /success:enable /failure:enable**

## Related topics

<dl> <dt>

[Auditpol](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc731451(v=ws.11))
</dt> <dt>

[Event Log](/previous-versions/orphan-topics/ws.10/dd996684(v=ws.10))
</dt> <dt>

[Group Policy](/windows/deployment/deploy-whats-new)
</dt> </dl>

