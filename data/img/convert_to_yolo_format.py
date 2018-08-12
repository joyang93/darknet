'''
to_player 0.12 0.13 0.12 0.1
 <class_number> (<absolute_x> / <image_width>) (<absolute_y> / <image_height>) (<absolute_width> / <image_width>) (<absolute_height> / <image_height>)
'''
import os

### text read
folder_1 = '/Users/smlee/Downloads/dial9193/label_split'
folder_2 = '/Users/smlee/Downloads/kmjui7/label_split'
folder_3 = '/Users/smlee/Downloads/pyopie/label_split'

folder_list = [folder_1, folder_2, folder_3]
for i,folder in enumerate(folder_list):
    width = 1280
    height = 720
    if i == 2:
        width = 1920
        height = 1080
    for txt_file in os.listdir(folder):
        rst = []
        f = open(os.path.join(folder,txt_file), 'r')
        lines = f.readlines()
        for line in lines:
            if line.find('player') != -1:
                text = line.split(',')

            # ratio calculate
                text[0] = float(text[0]) / float(width)
                text[1] = float(text[1]) / float(height)
                text[2] = float(text[2]) / float(width)
                text[3] = float(text[3]) /float(height)


               # 0 : ch_player 1: to_player
                if text[4].find('ch') != -1:
                    new_text = str(0) + ' ' + str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2]) + ' ' + str(text[3])
                else:
                    new_text = str(1) + ' ' + str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2]) + ' ' + str(text[3])

                rst.append(new_text)

        f.close()

        output_path = '/Users/smlee/Downloads/merge_txt'
        f = open(os.path.join(output_path,txt_file ), 'w')
        for data in rst:
            data = data + '\n'
            f.write(data)
        f.close()


