---
Description: 'The outbound routing rules you define can map outgoing fax jobs to particular devices or to fax device groups.'
ms.assetid: '59f6ef45-e7ae-4b62-a938-dfae13c22a7a'
title: Outbound Routing Rules
---

# Outbound Routing Rules

The outbound routing rules you define can map outgoing fax jobs to particular devices or to fax device groups. Before the fax service initiates a fax transmission, it checks the outbound routing rules to determine the rule that best matches the recipient telephone number. Once the fax service determines the best rule for the job, the service can also determine the device or the device group to which the rule points, and select the next available device in the group to send the fax.

You can use outbound routing rules to transmit faxes in the most cost-effective manner. For example, you could create a rule that specifies that all transmissions to area code 425 in the United States will use the *Carrier1* or the *Carrier2* device group because those device groups provide the best rate for recipient numbers with that area code.

If the fax service cannot map a recipient telephone number to a defined outbound routing rule, the service uses the default "All other" routing rule to send the fax. By default, the "All other" rule points to the "All devices" group. You can change the group to which the "All other" rule points.

## Related topics

<dl> <dt>

[**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)
</dt> <dt>

[**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md)
</dt> <dt>

[Creating and Managing Outbound Routing Rules (Visual Basic)](-mfax-creating-and-managing-outbound-routing-rules.md)
</dt> <dt>

[Creating Outbound Routing Rules (C++)](-mfax-creating-outbound-routing-rules-c.md)
</dt> </dl>

 

 



