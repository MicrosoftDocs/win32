---
description: The taxonomy described in this section first distinguishes the control plane that concerns itself with the way a multipoint session is established, from the data plane that deals with the transfer of data among session participants.
ms.assetid: f411acd7-5e33-4760-8a12-31c2d615426f
title: Multipoint Taxonomy
ms.topic: article
ms.date: 05/31/2018
---

# Multipoint Taxonomy

The taxonomy described in this section first distinguishes the control plane that concerns itself with the way a multipoint session is established, from the data plane that deals with the transfer of data among session participants.

## Session Establishment in the Control Plane

In the control plane there are two distinct types of session establishment:

-   rooted
-   nonrooted

In the case of rooted control, a special participant, c\_root, exists that is different from the rest of the members of this multipoint session, each of which are called a c\_leaf. The c\_root must remain present for the whole duration of the multipoint session, as the session is broken up in the absence of the c\_root. The c\_root usually initiates the multipoint session by setting up the connection to a c\_leaf, or a number of c\_leafs. The c\_root may add more c\_leafs, or (in some cases) a c\_leaf can join the c\_root at a later time. Examples of the rooted control plane can be found in ATM and ST-II.

For a nonrooted control plane, all the members belonging to a multipoint session are leaves, that is, no special participant acting as a c\_root exists. Each c\_leaf must add itself to a preexisting multipoint session that is always available (as in the case of an IP multicast address), or has been set up through some out-of-band (OOB) mechanism that is outside the scope of the Windows Sockets specification.

Another way to look at this is that a c\_root still exists, but can be considered to be in the network cloud as opposed to one of the participants. Because a control root still exists, a nonrooted control plane could also be considered to be implicitly rooted. Examples for this kind of implicitly rooted multipoint schemes are:

-   A teleconferencing bridge.
-   The IP multicast system.
-   A Multipoint Control Unit (MCU) in an H.320 video conference.

## Data Transfer in the Data Plane

In the data plane, there are two types of data transfer styles:

-   rooted
-   nonrooted

In a rooted data plane, a special participant called d\_root exists. Data transfer only occurs between the d\_root and the rest of the members of this multipoint session, each of which are referred to as a d\_leaf. The traffic could be unidirectional or bidirectional. The data sent out from the d\_root is duplicated (if required) and delivered to every d\_leaf, while the data from d\_leafs only goes to the d\_root. In the case of a rooted data plane, no traffic is allowed among d\_leafs. An example of a protocol that is rooted in the data plane is ST-II.

In a nonrooted data plane, all the participants are equal, that is, any data they send is delivered to all the other participants in the same multipoint session. Likewise each d\_leaf node can receive data from all other d\_leafs, and in some cases, from other nodes that are not participating in the multipoint session. No special d\_root node exists. IP-multicast is nonrooted in the data plane.

Note that the question of where data unit duplication occurs, or whether a shared single tree or multiple shortest-path trees are used for multipoint distribution are protocol issues, and irrelevant to the interface the application would use to perform multipoint communications. Therefore these issues are not addressed in this appendix or the Windows Sockets interface.

The following table depicts the taxonomy described above and indicates how existing schemes fit into each of the categories. Note that there do not appear to be any existing schemes that employ a nonrooted control plane along with a rooted data plane.

|                      | Rooted control plane | Nonrooted (implicit rooted) control plane |
|----------------------|----------------------|-------------------------------------------|
| Rooted data plane    | ATM, ST-II           | No known examples.                        |
| Nonrooted data plane | T.120                | IP-multicast, H.320 (MCU)                 |



 

 

 



