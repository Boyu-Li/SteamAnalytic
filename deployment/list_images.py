from nectar import ec2_conn

# print all available images
images = ec2_conn.get_all_images()
reservations = ec2_conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    print(i.__dict__)
#
# for img in images:
#     print('Image id: {}, image name: {}'.format(img.id, img.name))
