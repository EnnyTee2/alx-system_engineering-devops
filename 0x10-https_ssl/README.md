# 0x10. HTTPS SSL

## This directory covers tasks involving setting up SSL on my 'www.ennytee.tech' domain hosted in a previous project.
Some key requirements fulfilled are as follows:

* Configuring the domain zone so that the subdomain 'www' points to my load-balancer IP (lb-01).
* Terminating SSL on HAproxy which means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.
* Enforcing HTTPS so that no unencrypted traffic is possible and Configuring HAproxy to automatically redirect HTTP traffic to HTTPS.
