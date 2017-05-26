
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
### Instances

Does this show up?
{% for instance in account.instances %}

Does this show up
* Instance: {{instance.PrivateIpAddress}}
  * PublicDnsName = {{instance.PublicDnsName}}
  * PublicIpAddress = {{instance.PublicIpAddress}}
  * PrivateIpAddress = {{instance.PrivateIpAddress}}
  * PublicIp = {{instance.PublicIp}}
  * SubnetId = {{instance.SubnetId}}
  * PrivateIpAddress = {{instance.PrivateIpAddress}}

  {% endfor %}