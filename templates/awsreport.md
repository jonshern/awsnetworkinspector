
## Account
Profile Name: {{account.profilename }}

### VPC's
{% for vpc in account.vpcs %}
***
### Vpc: {{ vpc.VpcId }}
  * VpcId = {{ vpc.VpcId }}
  * CidrBlock = {{ vpc.VpcId }}
  * IsDefault = {{ vpc.IsDefault }}

#### Subnets
{% for subnet in vpc.subnets %}
* Subnet {{subnet.SubnetId}}
  * VpcId = {{subnet.VpcId}}
  * AvailabilityZone = {{subnet.AvailabilityZone}}
  * SubnetId = {{subnet.SubnetId}}
  * CidrBlock = {{subnet.CidrBlock}}
  * AssignIpv6AddressOnCreation = {{subnet.AssignIpv6AddressOnCreation}}
  * State = {{subnet.State}}
  {% endfor %}
{% endfor %}

***
### Elastic Ips
{% for eip in account.elasticips %}
* Elastic Ip: {{eip.PublicIp}}
  * NetworkInterfaceId = {{eip.NetworkInterfaceId}}
  * AssociationId = {{eip.AssociationId}}
  * NetworkInterfaceOwnerId = {{eip.NetworkInterfaceOwnerId}}
  * PublicIp = {{eip.PublicIp}}
  * AllocationId = {{eip.AllocationId}}
  * PrivateIpAddress = {{eip.PrivateIpAddress}}
  {% endfor %}

*** 
### Elastic Load Balancers
{% for elb in account.elasticloadbalancers %}
* ELB: {{elb.LoadBalancerName}}
  * PublicDnsName = {{elb.DNSName}}
  * PublicIpAddress = {{elb.LoadBalancerArn}}
  * PrivateIpAddress = {{elb.Scheme}}
  * PublicIp = {{elb.IpAddressType}}
 {% endfor %}
***
### Instances
{% for instance in account.instances %}
* Instance: {{instance.PrivateIpAddress}}
  * PublicDnsName = {{instance.PublicDnsName}}
  * PublicIpAddress = {{instance.PublicIpAddress}}
  * PrivateIpAddress = {{instance.PrivateIpAddress}}
  * PublicIp = {{instance.PublicIp}}
  * SubnetId = {{instance.SubnetId}}
  * PrivateIpAddress = {{instance.PrivateIpAddress}}
  {% endfor %}