---
Description: 'This topic tells you how to control verb visibility.'
title: How to Suppress and Control Verb Visibility
---

# How to Suppress and Control Verb Visibility

This topic tells you how to control verb visibility.

## Instructions

### 

You can use Windows policy settings to control verb visibility. Verbs can be suppressed through policy settings by adding a **SuppressionPolicy** subkey or a **SuppressionPolicyEx** GUID value to the verb's registry subkey. Set the value of the **SuppressionPolicy** subkey to the policy ID. If the policy is turned on, the verb and its associated shortcut menu entry are suppressed. For possible policy ID values, see the [**RESTRICTIONS**](restrictions.md) enumeration.

 

 



