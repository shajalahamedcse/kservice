### Configure The ssh config file for remote explorer  
    $ cd ~/.ssh/
    $ nano config


    Host kube-master
    HostName 65.0.5.9
    User ubuntu
    IdentityFile /Users/shajalahamed/Desktop/Training/devops3/opsclass/enviousOatmeal6uFakAvxR.pem


sudo docker build -t shajalahamecse/payment-service .