---
description: Recommendations to help choose the best Activity Coordinator policy.
ms.assetid: 512db72e-5153-4dad-a65c-831a05ab5b1c
title: Choose the right Activity Coordinator policy
ms.topic: article
ms.date: 04/27/2022
---

# Choose the right Activity Coordinator policy

## Understand your activity workload

Determine the Activity Coordinator Resources and the levels at which your activity workload consumes them. Profiling the task using a performance trace is a good place to start off.

## Choosing Resources

Choose resources derived from the performance trace. These resources should be the ones that your activity workload will have an impact on. Do not forget resources you implicitly consume or affect, such as user-idle and power.

## Choosing Conditions

Choose conditions based on the resource consumption of your workload, as observed in the performance trace. In general, we recommend using the best conditions for needed resources, and, if necessary, updating your policy with lesser conditions if it does not meet your needs within your desired timeframe. Starting with the best conditions and transitioning to lesser conditions is preferred before executing when your policy is not satisfied (its resource conditions aren’t satisfied) to meet any deadlines. For workloads with negligible or low resource consumption, conditions like **ACTIVITY_COORDINATOR_CONDITION_MEDIUM** may be usable without adversely affecting the system. Workloads with higher consumption are better suited to use conditions when resource availability is greater, like **ACTIVITY_COORDINATOR_CONDITION_GOOD**, but are more likely to cause impact when using lesser conditions. Keep in mind the types of devices and configurations your application supports in addition to the capabilities of the machine from any performance traces. Variability in the target environment may mean differences in how your workload impacts the system and the likelihood of your policy being satisfied over a given period.

## Deadline

There may be various time constraints associated with your activity. Longer running work or work that needs to begin or be completed in a relatively short amount of time may be better served using lesser conditions to increase the likelihood of the policy opening. Shorter running work or work that has loose time requirements may have their needs met using the best conditions. Over longer timeframes, the target system is likely to have periods of low resource consumption. If a deadline is approaching, we recommend downgrading your policy if sufficient progress hasn’t been made before resorting to regular execution methods after or on approach of the deadline. Reoccurring work can then switch to the original policy upon completion.

## Template policies

The API comes with a set of template policies for the typical work profile that can be used to trivially get started with the API. For most programs that do local computing, we recommend using the template policies.

## Policy recommendation

Of the provided template policies, if you aren’t sure about which one you should pick, the **ACTIVITY_COORDINATOR_POLICY_TEMPLATE_GOOD** should fit the bill for most cases. This policy will do a good job of avoiding interference, while providing a reasonable likelihood for the policy to be sufficiently open to complete the developer’s work.

## Customize template policies

Template policies may omit some resources (for example, GPU) which may not be required in general use cases. Based on the anticipated workload, a policy can be customized using the template policies as a starting point.

## Build policies from scratch

Developers who require full control can start from an empty policy: **ACTIVITY_COORDINATOR_POLICY_TEMPLATE_EMPTY**. However, for most scenarios it’s recommended that you start with **ACTIVITY_COORDINATOR_POLICY_TEMPLATE_BASE**, which specifies the minimum recommended resources that apply to most situations. This includes the user-idle, CPU, and power resources. Developers can then further customize it for their needs.

## Related topics

[Activity Coordinator API overview](activity-coordinator-api-overview.md)

[Activity Coordinator API and terminology](activity-coordinator-api-and-terminology.md)

[Activity Coordinator example project](activity-coordinator-example-project.md)
