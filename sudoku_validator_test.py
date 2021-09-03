class Sodoku_validator:
    def validate(self, sodoku_grid_to_validate):
        is_valid_ = True
        len_sodoku = len(sodoku_grid_to_validate)
        for iterator_index in range(len_sodoku):
            if(self.__double_exist(sodoku_grid_to_validate[iterator_index][x] for x in range(len_sodoku))):
                print("Double exist in row" + str(iterator_index))
                is_valid_ = False
            if(self.__double_exist(sodoku_grid_to_validate[x][iterator_index] for x in range(len_sodoku))):
                print("Double exist in row" + str(iterator_index))
                is_valid_ = False
        matrix_size = 3
        for row_iterator_index in range(matrix_size):
            for colum_iterator_index in range(matrix_size):
                if self.__double_exist(
                    sodoku_grid_to_validate[x + row_iterator_index * matrix_size][y + colum_iterator_index * matrix_size]
                    for x in range(matrix_size) for y in range(matrix_size)):
                        print(" Double exist in matrix" + str(row_iterator_index) + "- " +str(colum_iterator_index))
                        is_valid_ = False

        return is_valid_
    def __double_exist(self, list_of_numbers):
        list_of_numbers = list(filter(lambda x : x!=0, list_of_numbers))
        return (len(list_of_numbers) != len(set(list_of_numbers)))
