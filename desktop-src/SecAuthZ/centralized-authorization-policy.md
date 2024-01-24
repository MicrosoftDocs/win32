---
description: The Dynamic Access Control (DAC) scenario enables centralized access control administration for enterprise file server scenarios.
ms.assetid: 5A06B8D8-F14B-4D9E-9ED6-4246A26BF945
title: Centralized Authorization Policy
ms.topic: article
ms.date: 05/31/2018
---

# Centralized Authorization Policy

The [Dynamic Access Control (DAC) scenario](/previous-versions/windows/desktop/dacx/dynamic-access-control-developer-extensibility-roadmap) enables centralized access control administration for enterprise file server scenarios. Most organizations have multiple areas in which they want to control access.

Examples are:

-   Controlling access to sensitive information, in which files marked as sensitive would have specific permissions
-   Controlling access to files containing personally identifiable information (PII.)
-   Limiting access to documents based on the organizations retention policies.

Several new authorization policy abstractions are provided to allow an administrator to define these policies centrally and to simplify the definition process by allowing each of these access requirements to be defined and maintained separately but applied as one policy.

Two new Active Directory policy objects, a [central authorization policy](central-authorization-policies.md) (cap) and a [central authorization policy rule](central-authorization-policy-rule.md) (capr) are introduced in windows 8 to define and apply centralized authorization policies based on expressions of claims and resource attributes. in using these objects an administrator defines a capr as a specific authorization policy that can be applied to resources that have a certain attribute or satisfy a certain applicability condition. for example documents labeled as "high business impact". capes may be defined for each desired access control policy in an organization that can be expressed, and the resources to which it should be applied can be identified, in terms of windows 8 dac expressions. a cap is collection of caprs that can be applied together on resources. the following diagram shows the relationships of the cap and cape, and the conceptual steps involved in defining and applying these objects to file resources. ![relationship of capes and caps](images/cap.png)

 

 
