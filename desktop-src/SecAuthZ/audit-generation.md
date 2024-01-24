---
description: C2-level security requirements specify that system administrators must be able to audit security-related events and that access to this audit data must be limited to authorized administrators.
ms.assetid: 411001b1-94cd-465f-8558-c8aa119e4303
title: Audit Generation
ms.topic: article
ms.date: 05/31/2018
---

# Audit Generation

C2-level security requirements specify that system administrators must be able to audit security-related events and that access to this audit data must be limited to authorized administrators. The Windows API provides functions enabling an administrator to monitor security-related events.

The security descriptor for a securable object can have a [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). A SACL contains [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) that specify the types of access attempts that generate audit reports. Each ACE identifies a trustee, a set of access rights, and a set of flags that indicate whether the system generates audit messages for failed access attempts, successful access attempts, or both.

The system writes audit messages to the security event log. For information about accessing the records in a security event log, see [Event Logging](/windows/desktop/EventLog/event-logging).

To read or write an object's SACL, a thread must first enable the SE\_SECURITY\_NAME privilege. For more information, see [SACL Access Right](sacl-access-right.md).

The Windows API also provides support for server applications to generate audit messages when a client tries to access a private object. For more information, see [Auditing Access To Private Objects](auditing-access-to-private-objects.md).

 

 
