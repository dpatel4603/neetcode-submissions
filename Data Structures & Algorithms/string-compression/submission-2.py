class Solution:
    def compress(self, chars: List[str]) -> int:
        
       
        read = 0
        write = 0 

        n = len(chars)

        while read < n:
            char = chars[read]
            group_start = read


            while read < n and chars[read] == char:

                read += 1

            count = read - group_start

            chars[write] = char

            write += 1

            if count > 1:
                divisor = 1

                while divisor * 10 <= count:
                    divisor *= 10

                while divisor > 0:
                    chars[write] = str(count // divisor)
                    write += 1
                    count %= divisor
                    divisor //= 10

        return write

             

            